# Update Fleet
Update configuration files across a fleet of servers using Python and the secure copy protocol.

## Quickstart
Start by cloning the repo and changing your current directory to the project root.
```shell
$ cd ~/github
$ git clone https://github.com/adamturn/update-fleet.git && cd update-fleet
```

Next, create a /config directory and add a fleet.json file that contains a list of IPv4 addresses for each username key.
```shell
$ mkdir config
$ cp config-templates/template-fleet.json config/fleet.json
$ vi config/fleet.json
```
```json
{
    "ec2-user": ["101.100.99.98"],
    "root": ["127.0.0.1", "127.0.0.2"]
}
```

Then create an .ssh directory and add a fleet.pem file that contains RSA private keys for each server in the target fleet.
```shell
$ mkdir .ssh
$ cat ~/.ssh/example-server-one.pem >> fleet.pem
$ cat ~/.ssh/example-server-two.pem >> fleet.pem
```

Next: choose a target file for scp, copy it into /config, and edit it accordingly.
```shell
$ cp config-templates/template-config-dev.properties config/config-dev.properties
$ vi config/config-dev.properties
```

Project structure should now resemble something like this:
```
/update-fleet
    /.ssh
        fleet.pem
    /config
        config-dev.properties
        fleet.json
    /config-templates
        template-config-dev.properties
        template-fleet.json
    /src
        config-dev.py
        main.py
    .gitignore
    README.md
```

Finally, deploy a config file to a fleet of servers by running the main.py module and passing a relative path to each corresponding option.
```shell
$ python src/main.py id=.ssh/fleet.pem fleet=config/fleet.json file=config/config-dev.properties target=~/utils/config-dev.properties
```

Alternatively, save this configuration information in its own module to run independently like config_dev.py:
```python
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
```
