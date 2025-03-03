|[HOME](README.md)|[RESEARCH](01_research.md)|[INSTALLATION](02_install_rocky.md)|[CLIENT APP](03_client_app.md)|[INTEGRATION](04_wazuh_integration.md)|[DEMONSTRATION](05_demonstration.md)|[CONCLUSION](06_conclusion.md)|
|-|-|-|-|-|-|-|

# Install osquery on Rocky Linux (web01)

## Installation
- Install via yum repository (current version: 15.5.0) -- [source](https://osquery.io/downloads/official/5.15.0)
```bash
curl -L https://pkg.osquery.io/rpm/GPG | sudo tee /etc/pki/rpm-gpg/RPM-GPG-KEY-osquery
sudo yum install yum-utils -y
sudo yum-config-manager --add-repo https://pkg.osquery.io/rpm/osquery-s3-rpm.repo
sudo yum-config-manager --enable osquery-s3-rpm-repo
sudo yum install osquery
```
## Configuration
> [!Warning]
> Linux systems running journald will collect logging data originating from the kernel audit subsystem (something that osquery enables) from several sources, including audit records. To avoid performance problems on busy boxes (specially when osquery event tables are enabled), it is recommended to mask audit logs from entering the journal with the following command
> ```bash
> systemctl mask --now systemd-journald-audit.socket
> ```
> -- [source](https://osquery.readthedocs.io/en/latest/installation/install-linux/)

The `/etc/init.d/osqueryd` script does not automatically start the daemon until a configuration file is created. Create the default config file
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
|[<<<<](01_research.md)|[>>>>](03_client_app.md)|
|-|-|
