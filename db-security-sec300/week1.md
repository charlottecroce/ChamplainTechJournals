# Week1

Summary: Set up mysql, basic queries

### Install mysql-server:

* `sudo apt-get install mysql-server`

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdPFliHfcxJyOK9EcpTFg086E21yXVxgJZz5gXCXbOkiw8qH8kulFJy4MyjKOoJomBoFtsGkVgGWAMp5z3DMis_Hda2otT6KUCnSJhrDi6sZzykgYYmX3bsgqhLme2bggCzbXi1?key=aDi9OQh-ufWQEzuXd3URpoOQ)

* change bind address via `/etc/mysql/mysql.conf.d/mysqld.cnf`![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeGjZtbVFOHn9cjlkkew7w_A0YNNaGV5XepJ15r091W4LaWaj51D4BBdPFjT5N2TV6hhuMhYUaBPsrtPg9NfMVwhWyAK18DrNFUqG3HYBcgamPCs45LGOFHl2zGWdaO9t0-fLY?key=aDi9OQh-ufWQEzuXd3URpoOQ)
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

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdlvLE49RvjHQiyucG79dyVIohHu3qnyrDPOEFOOvUJEhIb8bxhtCT7ba8SkgWT-nVApwqg22IDQ5w8hx1TNCiSlhA9HMIgE_4mMvw8Ji-lz7CKvN33oG-ZdxW6NzVwJk_Vkcn8?key=aDi9OQh-ufWQEzuXd3URpoOQ)

* add data to table: `INSERT INTO requests (fname, email, rdate, uid) VALUES ( 'dummy', 'dummy@dummy.edu', '2024-11-12', 'nsk31fhenfJF024');`![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXc_GuGlbOQitjuCJbrgURaAGcqcndwuWmBpjxnpkbHUQ6x58zJtF2Q_xA9PyCKEbs9aOsatZAL6u80-fQHTBI1Eca5HpWurp8hSwfLD5sL_JoQNfaYJ8u8OwWmcbtxMDlZ2yFbI?key=aDi9OQh-ufWQEzuXd3URpoOQ)

### HW

![](<../.gitbook/assets/image (2).png>)

1: Write an SQL query that displays name and birth of cats whose names are Siggy

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXf_wUTuyRVkT6DUoJCL4ILqzz23ZzZlHl2PuKfbdpGRgFYAfWd2QKuyAZjJ2WRowefQSZA1Y4DIO-6YXcNZ7JyRs9LiG-F6bcGumW6MjZnod6iRY9h0Cl16AcQxEeceub1l2OZQ?key=aDi9OQh-ufWQEzuXd3URpoOQ)

2: Write an SQL query that displays name and birth of cats whose owners names are starting with the letter 'F'

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdBbRLxx7MylSUPgkJdsIZV-g6qP4f6CCI1TmryLwcWpN8bpYK62Lda1PYeY6Mfz0gMeNFHsoheL27e9mhPo0iEhE4TjWwHWPx5F9yy_UaA-cvFWJhPmgV8q_OOQIU7IHTM8rJL?key=aDi9OQh-ufWQEzuXd3URpoOQ)

3: Write an SQL query that displays the cat names, their owners names, and the birth of cats in single table for cats born in year 2020

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXe3LtKLAV8a8zVOgzyyKGdrXc0o7Vk60s4uTiFcImqlwAHbJRJNtDiyFZ_i8cmcmQtHPau2nJAjliZ73SJdKsW1vllJlzNDpTFBLeHtwPr086xFKktPgObUXKD5kOuHT-XijDYP?key=aDi9OQh-ufWQEzuXd3URpoOQ)

4: Write an SQL query that displays names of owners who has no cats

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdJo5G58de6UKRTEqe56CNrodFTDxlIVWyLP0zgLAtt0AEwW8AhsGDY1-gqdlgE9xJIrva-7lhBWypYgz6-IVrlj4KFDD3h3q2NNex4gInncKzer2Khs_2IUpZj-iVGj1dRX5dd?key=aDi9OQh-ufWQEzuXd3URpoOQ)
