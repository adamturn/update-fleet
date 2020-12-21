# Update Fleet
Update metadata files across a fleet of servers using Python and the secure copy protocol.

## Quickstart
Clone this repo and enter the project root.
```shell
$ cd ~/github
$ git clone https://github.com/adamturn/update-fleet.git && cd update-fleet
```

Make a fleet/ directory and add a "\<fleet-name\>.json" file with str username keys mapped to a list of str IPv4 addresses.
```shell
$ mkdir fleet
$ cp scp-templates/template-fleet.json scp-files/fleet.json
$ vi scp-files/fleet.json
```
```json
{
    "ec2-user": ["101.100.99.98"],
    "root": ["127.0.0.1", "127.0.0.2"]
}
```

Make a fleet/.ssh/ directory and add a "\<fleet-name\>.pem" file that contains private keys for each user@host combination in "\<fleet-name\>.json".
```shell
$ mkdir fleet/.ssh
$ cat ~/.ssh/example-server-one.pem >> fleet/.ssh/fleet.pem
$ cat ~/.ssh/example-server-two.pem >> fleet/.ssh/fleet.pem
```

Make an scp-files/ directory and add a file that you want to secure copy across the fleet.
```shell
$ mkdir scp-files
$ cp scp-templates/template-config-dev.properties scp-files/config-dev.properties
$ vi scp-files/config-dev.properties
```
```properties
env=DEV
host=127.0.0.1
user=username
pass=password
```

Project structure should now resemble this:
```
/update-fleet
    /fleets
        /.ssh
            fleet.pem
        fleet.json
    /scp-files
        config-dev.properties
    /scp-templates
        template-config-dev.properties
        template-fleet.json
    /src
        main.py
    .gitignore
    README.md
```

Finally, scp a file across a fleet of servers by running the "main.py" module with Python 3.6+. The fleet option requires your \<fleet-name\> and the scp option requires a full remote path with the file part matching one in your scp-files/ directory.
```shell
$ python src/main.py fleet=fleet scp=~/utils/config-dev.properties
```
