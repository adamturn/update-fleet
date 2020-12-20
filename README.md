# Update config-dev.properties files
Update configuration files across a fleet of servers using the secure copy protocol.

## Quickstart
Start by cloning the repo and changing your current directory to the project root.
```shell
$ cd ~/github
$ git clone https://github.com/adamturn/update-fleet.git && cd update-fleet
```

Next, define the target fleet with an /update-fleet/fleet.json file. Assign a list of IPv4 addresses to each username key:
```shell
$ touch fleet.json
```
```json
{
    "ec2-user": ["101.100.99.98"],
    "root": ["127.0.0.1", "127.0.0.2"]
}
```

Then create an /update-fleet/.ssh directory and add a fleet-config-dev.pem file that contains RSA private keys for each server in the target fleet. 
```shell
$ mkdir .ssh
$ cat ~/.ssh/example-server-one.pem >> fleet-config-dev.pem
$ cat ~/.ssh/example-server-two.pem >> fleet-config-dev.pem
```

Project structure should now look like this:
```
/update-fleet
    /.ssh
        fleet-config-dev.pem
    /src
        main.py
    /utils
        template-dev.properties
    .gitignore
    fleet.json
    README.md
```

Finally, deploy an updated ~/utils/config-dev.properties file to each server in the fleet by running the main module and passing the latest IPv4 address.
```shell
$ python src/main.py 192.0.0.1
```
