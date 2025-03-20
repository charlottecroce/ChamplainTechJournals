# LOG01 Configuration

> **Note**: This is the original log01 server that will eventually be retired, then brought back as a jump server.

## Basic Setup
- Set hostname to `log01-charlotte`
- Add sudo user `charlotte:password`
- Set network adapter to DMZ
- Configure static IP via nmtui:
  - IP Address: `172.16.50.5/29`
  - Gateway & DNS: `172.16.50.2`

## Configure Firewall for Syslog
```
sudo firewall-cmd --add-port=514/tcp --permanent
sudo firewall-cmd --add-port=514/udp --permanent
sudo firewall-cmd --reload
```

## Configure Rsyslog

### Enable Syslog Input Modules
Edit `/etc/rsyslog.conf` and uncomment these lines:
```
# Provides UDP syslog reception
module(load="imudp")
input(type="imudp" port="514")

# Provides TCP syslog reception
module(load="imtcp")
input(type="imtcp" port="514")
```

### Configure High Precision Timestamps
Add to `/etc/rsyslog.conf`:
```
$ActionFileDefaultTemplate RSYSLOG_SyslogProtocol23Format
template(name="BetterTiming" type="string" string="%timestamp:::date-rfc3339% %HOSTNAME% %syslogtag%%msg%\n")
```

Apply the template to the desired log file:
```
# Example: Add ;BetterTiming suffix to a log destination
*.info;mail.none;authpriv.none;cron.none                /var/log/messages;BetterTiming
```

### Configure Log Organization
Create a file named `/etc/rsyslog.d/sec350.conf` with these contents:
```
# Input modules
module(load="imudp")
input(type="imudp" port="514")
module(load="imtcp")
input(type="imtcp" port="514")

# Creating templates for storing logs dynamically
$template DynFile,"/var/log/%HOSTNAME%/%$YEAR%/%$MONTH%/%$DAY%/%programname%.log"
$template RemoteLogs,"/var/log/remote/%HOSTNAME%/%$YEAR%/%$MONTH%/%$DAY%/%programname%.log"

# Create a ruleset for remote devices
ruleset(name="RemoteDevice"){
    action(type="omfile" dynaFile="RemoteLogs")
}

# Direct local logs to files
:programname, !startswith, "rsyslog" ?DynFile

# Direct messages from remote hosts to the ruleset
:inputname, isequal, "imudp" call RemoteDevice
:inputname, isequal, "imtcp" call RemoteDevice
```

### Restart Rsyslog
```
sudo systemctl restart rsyslog
```

## Monitor Incoming Logs
```
tail -f /var/log/messages
```

Or check specific remote log files:
```
tail -f /var/log/remote/*/*/*/*/sshd.log
```

## Recommissioned as Jump Server
When log01 is repurposed as a jump server:

1. Change IP address to: `172.16.50.4/29`
2. Change hostname: `sudo hostnamectl set-hostname jump-charlotte`

### SSH Configuration for Passwordless Access
```bash
# Create dedicated user for jump access
useradd -m -d /home/charlotte-jump -s /bin/bash charlotte-jump

# Disable password authentication
sudo sed -i 's/PasswordAuthentication.*/PasswordAuthentication no/' /etc/ssh/sshd_config

# Create SSH directory structure with proper permissions
mkdir -p /home/charlotte-jump/.ssh
chmod 700 /home/charlotte-jump/.ssh

# Add the public key to authorized_keys
echo "ssh-rsa AAAAB3N...your-public-key..." >> /home/charlotte-jump/.ssh/authorized_keys

# Set proper permissions and ownership
chmod 600 /home/charlotte-jump/.ssh/authorized_keys
chown -R charlotte-jump:charlotte-jump /home/charlotte-jump/.ssh

# Restart SSH service
systemctl restart sshd
```

### Wazuh Agent Installation
```bash
sudo WAZUH_MANAGER='172.16.200.10' WAZUH_AGENT_GROUP='linux' WAZUH_AGENT_NAME='jump-charlotte' rpm -ihv wazuh-agent-4.7.3-1.x86_64.rpm
sudo systemctl daemon-reload
sudo systemctl enable wazuh-agent
sudo systemctl start wazuh-agent
```
