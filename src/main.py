"""
Python 3.6
Author: Adam Turner <turner.adch@gmail.com>
"""

# standard library
import json
import pathlib
import os
import subprocess
import sys
import time


def main(app_cfg: dict):
    start_time = time.time()
    src_dir = pathlib.Path(__file__).parent.absolute()
    if str(src_dir).endswith("src"):
        fleet_path = src_dir.parent / "fleet/{}.json".format(app_cfg[APP_CFG_KEY_0])
        remote_filepath = app_cfg[APP_CFG_KEY_1].strip()
        local_filepath = src_dir.parent / "scp-files/{}".format(remote_filepath.split("/")[-1])
        # host_prvkey = "~/.ssh/id_rsa"
    else:
        raise ValueError("Main module running outside of src directory!")

    with open(fleet_path, "r") as f:
        fleet = json.load(f)

    print("Updating...")
    for user in fleet:
        for ip_addr in fleet[user]:
            print(f"{user}@{ip_addr}")
            subprocess.run(
                ["scp", "-v", str(local_filepath), f"{user}@{ip_addr}:{remote_filepath}"],
                check=True
            )
    print(f"Update time: {time.time() - start_time} seconds")

    return None


if __name__ == "__main__":
    APP_CFG_KEY_0 = "fleet"
    APP_CFG_KEY_1 = "scp"
    APP_CFG = {APP_CFG_KEY_0: None, APP_CFG_KEY_1: None}
    for cmd_arg in sys.argv:
        for key in APP_CFG:
            if cmd_arg.startswith(key):
                APP_CFG[key] = cmd_arg.split("=")[1].strip()
    main(APP_CFG)
