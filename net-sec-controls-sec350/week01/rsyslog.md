# rsyslog configuration
an open-source software used on linux computer systems for forwarding log messages through a network. \
`sudo apt/yum install rsyslog`

## server
### open ports 514 on server
```
sudo firewall-cmd --add-port=514/tcp --permament
sudo firewall-cmd --add-port=514/udp --permament
sudo firewall-cmd --reload
```

### enable log input modules
the `/etc/rsyslog.conf` file needs to be modified to receive syslog messages over ports 514 tcp and udp. Uncomment the appropriate lines (see below) and restart the rsyslog service. \
![image](https://github.com/user-attachments/assets/48994d9b-0f17-4626-ab9d-985d37c5e506) 

### monitor for incoming logs
- `tail -f /var/log/messages`


## client
### configure log forwarding to server
- rsyslog needs to be installed on client as well: `sudo yum install rsyslog`
- create the following file: `/etc/rsyslog.d/sec350.conf`, add the line `user.notice @172.16.50.5`, and restart rsyslog
![image](https://github.com/user-attachments/assets/143d58a5-5713-4425-b1d5-d8f9dcf63cf0)

> **_NOTE:_** the line in sec350.conf means: \
> user = syslog facility \
> notice = syslog priority \
> @=UDP, @@ means TCP, so we are only going to send UDP \
> 172.16.50.5 = Remote Syslog Server

#### loggin authpriv messages on linux systems
![image](https://github.com/user-attachments/assets/77c2b1f5-6aa2-4e76-8db6-59feb31cb4fb)


### create test log
- `logger -t test TESTLOG123`
