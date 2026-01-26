[nmap docs](../nmap.md)

# opening ports on windows
## enable Remote Desktop Services on your windows 10 system using powershell. Run as administrator
```PowerShell
Set-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Terminal Server' -Name "fDenyTSConnections" -Value 0

Enable-NetFirewallRule -DisplayGroup "Remote Desktop"
```

## turn on file and print sharing
<img width="728" height="502" alt="image" src="https://github.com/user-attachments/assets/980a6e7f-9cdd-4bd6-9aaa-d3dffe39a778" />

# xfreerdp3
## installing xfreerdp3 on Kali
`echo $XDG_SESSION_TYPE`
Depending on if x11 or wayland
```
sudo apt install freerdp3-x11
or
sudo apt install freerdp3-wayland
```

## connect to rdp via xfreerpd3
```
sudo xfreerdp3 /v:10.0.17.54:3389 /u:champuser /p:'Ch@mpl@1n!25' /w:1366 /h:768 +clipboard
```


