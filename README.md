# Update Fleet
Update metadata files across a fleet of servers using Python and the secure copy protocol.

## Authorized Host
For this to work properly, the host running this program must have its public SSH key in the authorized_hosts file on every server in the fleet.
```shell
$ scp -i ~/.ssh/aws/aws-private-key.pem ~/.ssh/rsa_id.pub cloud-user@54.0.0.1:~/.ssh/tmp-public-key.pub
$ ssh -i ~/.ssh/aws/aws-private-key.pem cloud-user@54.0.0.1
[cloud-user]$ cat ~/.ssh/tmp-public-key.pub >> ~/.ssh/authorized_hosts
[cloud-user]$ rm ~/.ssh/tmp-public-key.pub && exit
```

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
    /fleet
        /.ssh
            id_rsa.pub
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
