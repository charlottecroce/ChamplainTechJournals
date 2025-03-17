|[HOME](README.md)|[RESEARCH](01_research.md)|[INSTALLATION](02_install_rocky.md)|[CLIENT APP](03_client_app.md)|[INTEGRATION](04_wazuh_integration.md)|[DEMONSTRATION](05_demonstration.md)|[CONCLUSION](06_conclusion.md)|
|-|-|-|-|-|-|-|

# Wazuh Integration

## Requirements
- Wazuh manager installed and configured on the wazuh server
- Wazuh agent installed and connected on WEB01
- osquery already installed on WEB01 ([installation guide](02_install_rocky.md))
- root privileges

## Configure osquery on web01
### on WEB01
- create osquery configuration file. if already created with defaults, edit it
```json
> sudo nano /etc/osquery/osquery.conf
{
  "options": {
    "config_plugin": "filesystem",
    "logger_plugin": "filesystem",
    "logger_path": "/var/log/osquery",
    "disable_logging": "false",
    "schedule_splay_percent": "10",
    "utc": "true"
    "output_format": "json"
  },
  "schedule": {
    "system_info": {
      "query": "SELECT hostname, cpu_brand, physical_memory FROM system_info;",
      "interval": 300
    },
    "processes": {
      "query": "SELECT pid, name, path, cmdline FROM processes;",
      "interval": 300
    },
    "logged_in_users": {
      "query": "SELECT user, host, time FROM logged_in_users;",
      "interval": 300
    },
    "firewall_status": {
      "query": "SELECT * FROM shell WHERE command = 'firewall-cmd --state';",
      "interval": 300
    }
  }
}
```

- create log directories with correct permissions for storing osquery results
```bash
sudo mkdir -p /var/log/osquery
sudo chown -R root:root /var/log/osquery
sudo chmod -R 755 /var/log/osquery
```

- restart osqueryd
```bash
sudo systemctl restart osqueryd
sudo systemctl status osqueryd
```

## Configure WEB01 -> Wazuh integration
### On WEB01
- configure Wazuh agent to monitor osquery logs
```xml
> sudo nano /var/ossec/etc/ossec.conf

# Add these blocks inside the <ossec_config> section
# make sure this wodle is NOT disabled, as this service is disabled by default

<wodle name="osquery">
  <disabled>no</disabled>
  <run_daemon>yes</run_daemon>
  <log_path>/var/log/osquery/osqueryd.results.log</log_path>
  <config_path>/etc/osquery/osquery.conf</config_path>
  <add_labels>yes</add_labels>
</wodle>


<localfile>
  <log_format>json</log_format>
  <location>/var/log/osquery/osqueryd.results.log</location>
</localfile>
```

- restart wazuh agent
```bash
sudo systemctl restart wazuh-agent
sudo systemctl status wazuh-agent
```

## Validation
### on WEB01
- Run a manual query to generate an immediate log entry
```
sudo osqueryi --json "SELECT * FROM processes LIMIT 5;" > /var/log/osquery/osqueryd.results.log
```
- Check if Wazuh detected it
```
sudo tail -f /var/ossec/logs/ossec.log
```
### on Wazuh Server
- Go to Modules Menu -> Security Events -> Events
- In left panel, add rule.groups: osquery
![image](https://github.com/user-attachments/assets/54a8264b-ffac-4f98-be7d-5d1abce24233)


___
|[<<<<](03_client_app.md)|[>>>>](05_demonstration.md)|
|-|-|

