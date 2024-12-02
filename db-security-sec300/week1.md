# Week1

Summary: Set up mysql, basic queries

### Install mysql-server:

* `sudo apt-get install mysql-server`

![{69DB5F3D-4FB8-4A3D-8310-5B03A26FC8D6}](https://github.com/user-attachments/assets/343d1a58-21fa-4b0d-8a37-7576de60c458)

* change bind address via `/etc/mysql/mysql.conf.d/mysqld.cnf`

![{16BE3259-B0A0-41FB-A311-B54C9CB89560}](https://github.com/user-attachments/assets/a3e74ced-e150-4892-b6e4-2945edbc1aac)

* remember! `sudo systemctl restart mysql`
* default password is found in `/etc/mysql/debian.cnf`
* first login: `sudo mysql -u root -p`
* show current users/DBs: `USE mysql;`, `SELECT User, Host FROM mysql.user;`, `SHOW DATABASES;`
* create registration DB: `CREATE DATABASE registration;`
* `USE registration;`
* create requests table:

```
CREATE TABLE requests(
id INT unsigned NOT NULL AUTO_INCREMENT,
fname VARCHAR(50) NOT NULL,
email VARCHAR(50) NOT NULL,
rdate DATE NOT NULL,
uid VARCHAR(15) NOT NULL,
PRIMARY KEY (id)
);
```

* show table: `DESCRIBE requests;`

![{2A6F6AA2-FF7F-4EDD-9B7E-798D32579173}](https://github.com/user-attachments/assets/cc6d2395-e631-4c69-a586-5cea6691d0a2)

* add data to table: `INSERT INTO requests (fname, email, rdate, uid) VALUES ( 'dummy', 'dummy@dummy.edu', '2024-11-12', 'nsk31fhenfJF024');`

![{B699A9A6-016F-4036-B4BD-92970B4F2C4C}](https://github.com/user-attachments/assets/060e33d0-03e7-487a-99bd-405356b81628)

### HW

![{DA8DD239-E048-47A2-B349-E2817F8F9E0D}](https://github.com/user-attachments/assets/e1886507-5613-4989-b671-a33d393fd9c3) ![{D52A57AE-75C2-45E9-AC30-04D9743D92E8}](https://github.com/user-attachments/assets/17cdb1f0-fc18-40fd-900c-e8c31c6c9a25) ![{75C712E2-ABF5-4BF3-BBE7-F39356C8D56E}](https://github.com/user-attachments/assets/3bc52487-c0b8-4ffb-97a5-7c7e710c98bb) ![{5399AB1C-4975-44B3-92D7-30A2FF1AA58E}](https://github.com/user-attachments/assets/b27c875f-d20f-4147-9846-fd97adbabc2a) ![{02A0D392-BEAE-45B7-97AF-E1793C76DBBD}](https://github.com/user-attachments/assets/04fe45c1-6fc0-44b5-a780-adf70eb295d7)

1: Write an SQL query that displays name and birth of cats whose names are Siggy

![{95573D20-9F7B-44E8-BB25-58461E11B90D}](https://github.com/user-attachments/assets/45b8918d-c1e8-4e5e-999b-72fddd688845)

2: Write an SQL query that displays name and birth of cats whose owners names are starting with the letter 'F'

![{18134315-4622-4453-97C8-B9D12CC90335}](https://github.com/user-attachments/assets/83aab27c-add8-4334-a0e8-78e090e5d71f)

3: Write an SQL query that displays the cat names, their owners names, and the birth of cats in single table for cats born in year 2020

![image](https://github.com/user-attachments/assets/e6b51d76-df56-42a0-954e-763d4cf427c3)

4: Write an SQL query that displays names of owners who has no cats

![image](https://github.com/user-attachments/assets/385a6c1e-473d-450d-a5c1-55cb4e77ec6c)
