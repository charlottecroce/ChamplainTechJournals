

Mysqld configuration on Kali
```
sudo systemctl enable mysqld
sudo systemctl start mysqld
sudo mysql_secure_installation

#
switch to unix_socket auth: n
change root passwd: y
remove anon users: y
disallow remote toot: y
remote test DB: y
reload priv tables now: y
```

clone the sqli-labs-php git repository
```
sudo git clone https://github.com/skyblueee/sqli-labs-php7.git
cd sqli-labs-php7.git

# remote .git so no github issues
sudo rm .git -rf
```
- edit sql-connections/db-creds.inc to have DB root password just set

start php server
```
sudo php -S 127.0.0.1:8090 -t .
```
<img width="706" height="361" alt="image" src="https://github.com/user-attachments/assets/2b89be76-450d-4b15-b640-0c98d1482d2b" />

add these lines for increased error handling and debug statements

<img width="648" height="530" alt="image" src="https://github.com/user-attachments/assets/019d3b93-3a44-4392-8b64-80a4ccc02a85" />

<img width="838" height="315" alt="image" src="https://github.com/user-attachments/assets/44eaef21-9a28-4caf-acb8-70b655ef905c" />
