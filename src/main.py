"""
Python 3.6
Author: Adam Turner <turner.adch@gmail.com>
"""

# standard library
import json
import os
import pathlib
import re
import subprocess
import sys
import time


def remove_tmp(filepath=None, dirpath=None):
    if filepath:
        os.remove(filepath)
    if dirpath:
        os.rmdir(dirpath)

    return None


def main(host: str):
    src_dir = pathlib.Path(__file__).parent.absolute()
    if str(src_dir).endswith("src"):
        # TODO: fleet-config-dev.pem is added manually
        pem_path = src_dir.parent / ".ssh/fleet-config-dev.pem"
        template_path = src_dir.parent / "utils/template-dev.properties"
    else:
        raise ValueError("Program running outside of /src directory!")

    with open(template_path, "r") as template_file:
        template_text = template_file.read()

        tmp_dir = src_dir.parent / "tmp"
        config_name = "config-dev.properties"
        config_path = tmp_dir / config_name

        try:
            os.mkdir(tmp_dir)
        except FileExistsError:
            remove_tmp(config_path, tmp_dir)
            os.mkdir(tmp_dir)
  
        with open(config_path, "w") as config_file:
            updated_text = re.sub(pattern=r"<CMD_ARG>", repl=host, string=template_text)
            config_file.write(updated_text)
            print(f"Updated config:\n{updated_text}")

    fleet_path = src_dir.parent / "fleet.json"
    with open(fleet_path, "r") as f:
        fleet = json.load(f)

    print("Updating...")
    target_path = f"~/utils/{config_name}"
    for user in fleet:
        for ip_addr in fleet[user]:
            print(f"{user}@{ip_addr}")
            # print(f"scp -i {str(pem_path)} {str(config_path)} {user}@{ip_addr}:{target_path}")
            subprocess.run(
                ["scp", "-i", str(pem_path), str(config_path), f"{user}@{ip_addr}:{target_path}"],
                check=True
            )
            continue

    print("Removing tmp files...")
    remove_tmp(config_path, tmp_dir)

    return None


if __name__ == "__main__":
    start_time = time.time()
    CMD_ARG = sys.argv[-1].strip()
    if re.match(pattern=r"^(\d{1,3}\.){3}\d{1,3}\s*$", string=CMD_ARG):
        main(host=CMD_ARG)
    else:
        raise ValueError(f"\'{CMD_ARG}\' is not a valid IPv4 address!")
    print(f"Update time: {time.time() - start_time} seconds")
    