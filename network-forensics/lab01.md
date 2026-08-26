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



create client config file

./velociraptor --config server.config.yaml config client > client.config.yaml




sed -e '/bind_address:/{s/127.0.0.1/10.0.3.117/}' -i /etc/velociraptor/server.config.yaml


- now velociraptor_server is a service you can control with systemctl
- you can access the dashboard at https://localhost:8889



