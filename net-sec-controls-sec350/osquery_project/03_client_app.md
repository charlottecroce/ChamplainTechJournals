|[HOME](README.md)|[RESEARCH](01_research.md)|[INSTALLATION](02_install_rocky.md)|[CLIENT APP](03_client_app.md)|[INTEGRATION](04_wazuh_integration.md)|[DEMONSTRATION](05_demonstration.md)|[CONCLUSION](06_conclusion.md)|
|-|-|-|-|-|-|-|

# osquery Client Application (osqueryi)
`osqueryi` is an interactive shell for osquery that uses SQL-like queries to gather system information. It allows you to query various aspects of an operating system as if they were tables in a database.

## Common queries:
Inspect system processes:
```sql
osquery> SELECT name, path, pid FROM processes WHERE name = 'httpd';
+-------+-----------------+-------+
| name  | path            | pid   |
+-------+-----------------+-------+
| httpd | /usr/sbin/httpd | 82243 |
| httpd | /usr/sbin/httpd | 86173 |
| httpd | /usr/sbin/httpd | 86174 |
| httpd | /usr/sbin/httpd | 86175 |
| httpd | /usr/sbin/httpd | 86176 |
+-------+-----------------+-------+
```
List installed packages:
```sql
osquery> SELECT name, version FROM rpm_packages;
+-------------------------------+------------+
| name                          | version    |
+-------------------------------+------------+
| NetworkManager                | 1.36.0     |
| NetworkManager-config-server  | 1.36.0     |
| NetworkManager-libnm          | 1.36.0     |
| NetworkManager-team           | 1.36.0     |
| NetworkManager-tui            | 1.36.0     |
| acl                           | 2.2.53     |
| adcli                         | 0.8.2      |
| alsa-sof-firmware             | 1.9.3      |
| apr                           | 1.6.3      |
| apr-util                      | 1.6.1      |
...
```
Check listening network ports:
```sql
osquery> SELECT pid, address, port FROM listening_ports;
+-------+-----------+-------+
| pid   | address   | port  |
+-------+-----------+-------+
| 1101  | 0.0.0.0   | 22    |
| 86176 | ::        | 80    |
| 1101  | ::        | 22    |
| 34468 | 0.0.0.0   | 51361 |
| 942   | 127.0.0.1 | 323   |
| 942   | ::1       | 323   |
| 1068  | ::        | 58    |
| 924   |           | 0     |
| 924   |           | 0     |
...
```

___
|[<<<<](02_install_rocky.md)|[>>>>](04_wazuh_integration.md)|
|-|-|
