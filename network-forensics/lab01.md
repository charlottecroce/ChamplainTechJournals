# Lab01

- https://prox.df.local

|Host|IP|Server|Credentials|
|-|-|-|-|
|ROUTER|10.3.10.254, 10.100.10.108|df-1||
|SRV03|10.3.10.154|df-1||
|DC01|10.3.10.179|df-1||
|DC03|10.3.10.131|df-2||
|Win11|10.3.10.251|df-2|champuser:Ch@mpl@1n!26|
|SRV02|10.3.10.110|df-3||
|Kali|10.3.10.99|df-3|kali:kali|
|Ubuntu|10.3.10.117|df-3|champuser:Ch@mpl@1n!26|
|DC02|10.3.10.211|df-4||

## Sysmon Config Pusher

on windows 10:
### Download Sysmon:
- Visit the official Sysinternals page: https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon.
    - Download the Sysmon executable and the Sysmon Configuration file:
    - use this config file (https://raw.githubusercontent.com/olafhartong/sysmon-modular/master/sysmonconfig.xml)



## Download Velociraptor
- https://docs.velociraptor.app/downloads/
  - download velociraptor-v0.77.2-linux-amd64
- move to /opt/velociraptor
- rename to just velociraptor for convienience

```
chmod +x velociraptor
sudo ./velocirapto config generate -i
```
  - Self-Signed SSL, no registry, set DNS to the IP(10.3.10.117)
    - Creds: charlotte:FOR440!

```
./velociraptor --config server.config.yaml debian server
apt install velociraptor-xyz.deb
```


- now velociraptor_server is a service you can control with systemctl
- you can access the dashboard at https://localhost:8889

## create client config file

./velociraptor --config server.config.yaml config client > client.config.yaml

copy this to the windows client
also on the windows client download the velociraptor exe. server and client use the same downloaded file

./velociraptor-xyz.exe --config ./client.config.yaml service install

## on the ubuntu machine

sed -e '/bind_address:/{s/127.0.0.1/10.0.3.117/}' -i /etc/velociraptor/server.config.yaml
change GUI bind_address to 0.0.0.0


remember now that this is a service the config is in /etc/velociraptor and not opt anymore






