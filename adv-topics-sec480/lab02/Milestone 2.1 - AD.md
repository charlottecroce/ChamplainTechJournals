# Milestone 2.1 - AD

## installing windows server
- pull win server 2019 ISO to ESXI datastore
- new VM (480-ad-charlotte):  2cpu 4gb RAM, 90gb HDD, Network adapter on VMNet for now, thin provisioned
- select standard desktop experience
- dont set admin password, on admin pw prompt, use CTRL+SHIFT+F3 to enter audit mode. ignore system prep tool popup
- Open Powershell > `sconfig`
  - 5: Change to manual windows updates
  - 9: Change timezone to Eastern
  - 6: Install updates - ALL (you will need an internet connection)
    - this will take up to an hour


## install VMware Tools
- Right click in host console, guest OS - install vmware tools, this mounts to VM, then run in OS (typical)


## sysprep
- restart after installing VMware tools
- you can get the commands via https://tinyurl.com/480sysprep
- run each line individually in order
```PowerShell
Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0
Start-Service sshd
# a good time to complete via remote ssh
Set-Service -Name sshd -StartupType 'Automatic'
Set-ItemProperty "HKLM:\Software\Microsoft\Powershell\1\ShellIds" -Name ConsolePrompting -Value $true
New-ItemProperty -Path HKLM:\SOFTWARE\OpenSSH -Name DefaultShell -Value "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe" -PropertyType String -Force
#Write-Host "Create a deployer user: Enter Password"
#$pw = Read-Host -AsSecureString
#New-LocalUser -Name deployer -Password $pw -AccountNeverExpires -PasswordNeverExpires:$true
#Add-LocalGroupMember -Group Administrators -Member deployer
Write-Host "Pull down unattend.xml and then sysprep the box"
wget https://raw.githubusercontent.com/gmcyber/RangeControl/main/src/scripts/base-vms/windows/unattend.xml -Outfile C:\Unattend.xml

# WHEN YOU REACH HERE, STOP AND REBOOT

C:\Windows\System32\Sysprep\sysprep.exe /oobe /generalize /unattend:C:\unattend.xml
Write-Host "Set Power to High Performance"
powercfg -setactive 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c
```
- when complete, remove ISO from drive
- make sure you’re VM is powered off and take a snapshot, name it `Base`
- now we have a clean snapshot of windows server 2019 we can use in future labs


## ad setup - remotely from xubuntu machine via powershell commands
- Change the network segment to 480-internal (from VM Network): only step that has to be done via ESXI
- set IP / gateway / dns
```PowerShell
Get-NetIPConfiguration
New-NetIPAddress -InterfaceIndex 12 -IPAddress 10.0.17.4 -PrefixLength 24 -DefaultGateway 10.0.17.2
Set-DnsClientServerAddress -InterfaceIndex 12 -ServerAddresses "10.0.17.2"
```
- Add the Administrative user password
```PowerShell
Set-ADAccountPassword -Identity "Administrator" -Reset -NewPassword "sec480480!"
```
- rename computer (will restart)
```PowerShell
Rename-Computer -NewName "dc1" -Restart
```

- install adds
```
# install AD DS role and management tools
Install-WindowsFeature -Name AD-Domain-Services -IncludeManagementTools
# create a new forest
Import-Module ADDSDeployment
Install-ADDSForest -DomainName "charlotte.local" -InstallDNS
```
- install dns
```
# install DNS role and management tools
Install-WindowsFeature -Name DNS -IncludeManagementTools
```



