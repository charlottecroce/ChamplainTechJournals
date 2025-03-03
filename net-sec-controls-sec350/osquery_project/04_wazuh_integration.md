|[HOME](README.md)|[RESEARCH](01_research.md)|[INSTALLATION](02_install_rocky.md)|[CLIENT APP](03_client_app.md)|[INTEGRATION](04_wazuh_integration.md)|[DEMONSTRATION](05_demonstration.md)|[CONCLUSION](06_conclusion.md)|
|-|-|-|-|-|-|-|

# Wazuh Integration



___
|[<<<<](03_client_app.md)|[>>>>](05_demonstration.md)|
|-|-|

## Configuration 

# Install yum-utils 

`curl -L https://pkg.osquery.io/rpm/GPG | tee /etc/pki/rpm-gpg/RPM-GPG-KEY-osquery
yum-config-manager --add-repo https://pkg.osquery.io/rpm/osquery-s3-rpm.repo
yum-config-manager --enable osquery-s3-rpm-repo
yum install osquery`

# Configuration Setup

This is the command to copy the existing example config file into your working config files directory, this file may need further configuration. 

`cp /opt/osquery/share/osquery/osquery.example.conf /etc/osquery/osquery.conf`

Run these commads to start osquery

`sysetmctl enable osqueryd`
`systemctl start osqueryd`


Source: https://documentation.wazuh.com/current/user-manual/capabilities/system-inventory/osquery.html#configuration 

