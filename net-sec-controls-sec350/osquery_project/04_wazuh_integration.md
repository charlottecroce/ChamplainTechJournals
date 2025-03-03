|[HOME](README.md)|[RESEARCH](01_research.md)|[INSTALLATION](02_install_rocky.md)|[CLIENT APP](03_client_app.md)|[INTEGRATION](04_wazuh_integration.md)|[DEMONSTRATION](05_demonstration.md)|[CONCLUSION](06_conclusion.md)|
|-|-|-|-|-|-|-|

# Wazuh Integration
## DMZ-to-WAN temporary firewall rule
Add a temporary rule for software updates that we either delete, disable or discard when complete
```bash
set firewall name DMZ-to-WAN rule 999 action accept
set firewall name DMZ-to-WAN rule 999 source address 172.16.50.3
```



___
|[<<<<](03_client_app.md)|[>>>>](05_demonstration.md)|
|-|-|
