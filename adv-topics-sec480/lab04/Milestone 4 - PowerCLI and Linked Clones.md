# Milestone 4 - PowerCLI and Linked Clones

## setting up PowerCLI on xubuntu
Install PowerShell on mgmt
```
sudo snap install powershell --classic
pwsh
```
PowerCLI Libraries
```
Install-Module VMware.PowerCLI -Scope CurrentUser
Get-Module VMware.PowerCLI -ListAvailable
Set-PowerCLIConfiguration -InvalidCertificateAction Ignore
Set-PowerCLIConfiguration -Scope User -ParticipateInCEIP $false
```
onboard is useful to execute function commands in the vcenter console like F2

```
sudo apt install remmina onboard
```
testing connectivity
```
Connect-VIServer -Server 10.0.17.3
>>> you can login as charlotte-adm@charlotte.local
Get-VM
exit
```
<img width="511" height="379" alt="{B4390C27-6DC0-4CDF-B05D-45D9BF32218E}" src="https://github.com/user-attachments/assets/316b5408-0304-4817-8a26-fda1506246e2" />

install vscode (for ease of scripting, min 4GB memory)
```
sudo snap install code --classic
```

