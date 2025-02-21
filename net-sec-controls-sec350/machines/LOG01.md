# LOG01 Configuration

> **Note**: This is the original log01 server that will eventually be retired.

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
