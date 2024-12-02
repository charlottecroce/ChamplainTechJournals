# Week2

## DB Webserver Connection

* create user for remote access:

![](https://github.com/user-attachments/assets/f8f506c8-0f40-4ff6-90eb-38b9ff25b709)

* allow connections through firewall: `sudo ufw allow from 0.0.0.0 to 0.0.0.0 port 3306 proto tcp`
* get python dependencies: `sudo apt update && sudo apt install python3 python3-pip python3-venv`
* `cd /home/champuser/proj/`
* create virtual environment: `python3 -m venv .venv` activate: `. .venv/bin/activate`

install flask: pip install flask

Create directory for Flask: mkdir Flask, cd Flask

dependencies pip install Flask-MySQLdb pip install flask-mysql pip install cryptography

![](https://github.com/user-attachments/assets/df863553-d342-40f2-b486-95c9f96eb6ab)

![](https://github.com/user-attachments/assets/ff0e2ea6-8d9b-419e-87bc-e509607ec2c3)

![](https://github.com/user-attachments/assets/ecfef5d2-faf0-48a2-890a-d7a8828d8070)

![](https://github.com/user-attachments/assets/f1ee877f-5ecc-439c-af72-3e66b7cad0f7)

![](https://github.com/user-attachments/assets/b364793f-b228-4496-8129-aaf87125bfc6)

if localhost doesn't work, change bind-address in /etc/mysql/mysql.conf.d/mysqld.cnf

## Filter from application

* add form action ![image](https://github.com/user-attachments/assets/5d975c40-abd8-4d1d-807c-b1ea1c9f47bf)
* add python form processing ![image](https://github.com/user-attachments/assets/0710091e-53e4-46a0-a94c-3f82ac255c96)

## for pets db

![](https://github.com/user-attachments/assets/99c577de-f2fa-45fe-91c4-e9c780e4ed95)
