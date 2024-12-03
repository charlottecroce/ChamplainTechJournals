# Week4
Log analysis

- `sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf`

![image](https://github.com/user-attachments/assets/8c9e506d-5da1-4907-8773-2ef2dc7cd53b)


- Display failed connect logs, display only date, time, and user
```
cat /var/log/mysql/query.log | awk -F"[[:space:]T]+" '/Access denied/ {print $1,$2,$9}'
```

- Display successful connect logs, display only date, time, and user
```
cat /var/log/mysql/query.log | awk -F"[[:space:]T]+" '/Connect/ {print $1,$2,$5}' | grep -v 'Access'
```
