"""
Python 3.6
Author: Adam Turner <turner.adch@gmail.com>
"""

# local modules
from main import main


def config_dev():
    file_name = "config-dev.properties"
    app_cfg = {
        "fleet": "config/fleet.json",
        "id": ".ssh/fleet.pem",
        "file": f"config/{file_name}",
        "target": f"~/utils/{file_name}"
    }

    return app_cfg


if __name__ == "__main__":
    main(config_dev())
