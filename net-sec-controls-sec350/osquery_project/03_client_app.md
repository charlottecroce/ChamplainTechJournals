|[HOME](https://github.com/charlottecroce/ChamplainTechJournals/blob/main/net-sec-controls-sec350/osquery_project/README.md)|[RESEARCH](https://github.com/charlottecroce/ChamplainTechJournals/blob/main/net-sec-controls-sec350/osquery_project/01_research.md)|[INSTALLATION](https://github.com/charlottecroce/ChamplainTechJournals/blob/main/net-sec-controls-sec350/osquery_project/02_install_rocky.md)|[CLIENT APP](https://github.com/charlottecroce/ChamplainTechJournals/blob/main/net-sec-controls-sec350/osquery_project/03_client_app.md)|[INTEGRATION](https://github.com/charlottecroce/ChamplainTechJournals/blob/main/net-sec-controls-sec350/osquery_project/04_wazuh_integration.md)|[DEMONSTRATION](https://github.com/charlottecroce/ChamplainTechJournals/blob/main/net-sec-controls-sec350/osquery_project/05_demonstration.md)|[CONCLUSION](https://github.com/charlottecroce/ChamplainTechJournals/blob/main/net-sec-controls-sec350/osquery_project/06_conclusion.md)|
|-|-|-|-|-|-|-|

# osquery Client Application (osqueryi)
`osqueryi` is an interactive shell for osquery that uses SQL-like queries to gather system information. It allows you to query various aspects of an operating system as if they were tables in a database.

## Common queries:
Inspect system processes:
```sql
SELECT name, path, pid FROM processes WHERE name = 'httpd';
```
List installed packages:
```sql
SELECT name, version FROM rpm_packages;
```
Check listening network ports:
```sql
SELECT pid, address, port FROM listening_ports;
```

___
|[<<<<](https://github.com/charlottecroce/ChamplainTechJournals/blob/main/net-sec-controls-sec350/osquery_project/02_install_rocky.md)|[>>>>](https://github.com/charlottecroce/ChamplainTechJournals/blob/main/net-sec-controls-sec350/osquery_project/04_wazuh_integration.md)|
|-|-|
