|[HOME](README.md)|[RESEARCH](01_research.md)|[INSTALLATION](02_install_rocky.md)|[CLIENT APP](03_client_app.md)|[INTEGRATION](04_wazuh_integration.md)|[DEMONSTRATION](05_demonstration.md)|[CONCLUSION](06_conclusion.md)|
|-|-|-|-|-|-|-|

# Research
Osquery is an open-source OS instrumentation framework that uses SQL-like syntax to query the OS as if it were a relational database. It was created by Facebook(Meta) in 2014.

## Features
- **Cross-platform**: macOS, Linux, FreeBSD, and Windows
- **Data collection**: running processes, user logins, kernel modules, network connections, browser plugins, hardware events, file hashes, and more
- **SQL-based queries**: Users can write SQL queries to explore data across all operating systems and infrastructure
- **Query packs**: Pre-built collections of queries for specific tasks like incident response, vulnerability management, or compliance monitoring

## Components
1. [**Osqueryi**](03_client_app.md): An interactive console shell for running ad-hoc queries and exploring the system
2. [**Osqueryd**](02_install_rocky.md): A daemon that schedules queries and monitors system changes

> [!Warning]
> Osquery generates approximately 110MB of data per endpoint per day. This requires careful consideration of storage and management, especially for large-scale deployments.

Sources:
- https://www.uptycs.com/blog/threat-research-report-team/osquery-guide
- https://rearc.io/blog/osquery-introduction
- https://www.rapid7.com/blog/post/2016/05/09/introduction-to-osquery-for-threat-detection-dfir/

___
|[<<<<](README.md)|[>>>>](02_install_rocky.md)|
|-|-|
