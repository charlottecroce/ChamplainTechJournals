|[HOME](README.md)|[RESEARCH](01_research.md)|[INSTALLATION](02_install_rocky.md)|[CLIENT APP](03_client_app.md)|[INTEGRATION](04_wazuh_integration.md)|[DEMONSTRATION](05_demonstration.md)|[CONCLUSION](06_conclusion.md)|
|-|-|-|-|-|-|-|

# Install osquery on Rocky Linux (web01)

## Installation
### DMZ-to-WAN temporary firewall rule
Add a temporary rule for software updates that we either delete, disable or discard when complete
```bash
set firewall name DMZ-to-WAN rule 999 action accept
set firewall name DMZ-to-WAN rule 999 source address 172.16.50.3
```
### Install via yum repository
- (current version: 15.5.0) -- [source](https://osquery.io/downloads/official/5.15.0)
```bash
curl -L https://pkg.osquery.io/rpm/GPG | sudo tee /etc/pki/rpm-gpg/RPM-GPG-KEY-osquery
sudo yum install yum-utils -y
sudo yum-config-manager --add-repo https://pkg.osquery.io/rpm/osquery-s3-rpm.repo
sudo yum-config-manager --enable osquery-s3-rpm-repo
sudo yum install osquery -y
```
## Configuration
> [!Warning]
> Linux systems running journald will collect logging data originating from the kernel audit subsystem (something that osquery enables) from several sources, including audit records. To avoid performance problems on busy boxes (specially when osquery event tables are enabled), it is recommended to mask audit logs from entering the journal with the following command
> ```bash
> systemctl mask --now systemd-journald-audit.socket
> ```
> -- [source](https://osquery.readthedocs.io/en/latest/installation/install-linux/)

The `/etc/init.d/osqueryd` script does not automatically start the daemon until a configuration file is created. This is the command to copy the existing example config file into your working config files directory, this file may need further configuration. 
```bash
sudo cp /opt/osquery/share/osquery/osquery.example.conf /etc/osquery/osquery.conf
```

## Running osquery
### Standalone/Client App (osqueryi)
To start a standalone osquery use: `osqueryi`. This does not need an osquery server or service. [osqueryi page](03_client_app.md)

### Daemon Service (osqueryd)
```bash
sudo systemctl enable osqueryd
sudo systemctl start osqueryd
```

> [!Note]
> The interactive shell and daemon do NOT communicate!



___
Source: https://documentation.wazuh.com/current/user-manual/capabilities/system-inventory/osquery.html 

|[<<<<](01_research.md)|[>>>>](03_client_app.md)|
|-|-|
