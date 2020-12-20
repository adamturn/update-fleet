"""
Python 3.6
Author: Adam Turner <turner.adch@gmail.com>
"""

# standard library
import json
import pathlib
import subprocess
import sys
import time


def main(app_cfg: dict):
    start_time = time.time()
    src_dir = pathlib.Path(__file__).parent.absolute()
    if str(src_dir).endswith("src"):
        # TODO: fleet-config-dev.pem is added manually
        pem_path = src_dir.parent / app_cfg["id"]
        fleet_path = src_dir.parent / app_cfg["fleet"]
        file_path = src_dir.parent / app_cfg["file"]
        target_path = app_cfg["target"]
    else:
        raise ValueError("Program running outside of /src directory!")

    with open(fleet_path, "r") as f:
        fleet = json.load(f)

    print("Updating...")
    for user in fleet:
        for ip_addr in fleet[user]:
            print(f"{user}@{ip_addr}")
            subprocess.run(
                ["scp", "-i", str(pem_path), str(file_path), f"{user}@{ip_addr}:{target_path}"],
                check=True
            )
            continue
    print(f"Update time: {time.time() - start_time} seconds")

    return None


if __name__ == "__main__":
    APP_CFG = {"fleet": None, "id": None, "file": None, "target": None}
    for CMD_ARG in sys.argv:
        for option in APP_CFG:
            if CMD_ARG.startswith(option):
                APP_CFG[option] = CMD_ARG.split("=")[1].strip()
    main(APP_CFG)
