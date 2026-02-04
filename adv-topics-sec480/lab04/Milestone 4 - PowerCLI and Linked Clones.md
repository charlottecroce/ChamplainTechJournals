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

## creating win server 2019 clone via PowerCLI
```
#Connect
$vserver="vcenter.charlotte.local"
Connect-VIServer($vserver)
#Source VM
$vm=Get-VM -Name 480-ad-charlotte
$snapshot = Get-Snapshot -VM $vm -Name "Base"
$vmhost = Get-VMHost -Name 192.168.3.205
$ds=Get-DataStore -Name datastore2
$linkedname = "{0}.linked" -f $vm.name
#Create the tempory VM
$linkedvm = New-VM -LinkedClone -Name $linkedName -VM $vm -ReferenceSnapshot $snapshot -VMHost $vmhost -Datastore $ds
#Create the Full VM
$newvm = New-VM -Name "server.2019.base" -VM $linkedvm -VMHost $vmhost -Datastore $ds
#A new Snap Shot
$newvm | new-snapshot -Name "Base"
#Cleanup the temporary linked clone
$linkedvm | Remove-VM
```

## creating xubuntu clone via PowerCLI
```
#Connect
$vserver="vcenter.charlotte.local"
Connect-VIServer($vserver)
#Source VM
$vm=Get-VM -Name 480-mgmt-charlotte
$snapshot = Get-Snapshot -VM $vm -Name "2-4"
$vmhost = Get-VMHost -Name 192.168.3.205
$ds=Get-DataStore -Name datastore2
$linkedname = "{0}.linked" -f $vm.name
#Create the tempory VM
$linkedvm = New-VM -LinkedClone -Name $linkedName -VM $vm -ReferenceSnapshot $snapshot -VMHost $vmhost -Datastore $ds
#Create the Full VM
$newvm = New-VM -Name "mgmt.base" -VM $linkedvm -VMHost $vmhost -Datastore $ds
#A new Snap Shot
$newvm | new-snapshot -Name "Base"
#Cleanup the temporary linked clone
$linkedvm | Remove-VM
```

## creating win server 2019 clone via PowerCLI
```
#Connect
$vserver="vcenter.charlotte.local"
Connect-VIServer($vserver)
#Source VM
$vm=Get-VM -Name 480-fw-charlotte
$snapshot = Get-Snapshot -VM $vm -Name "2-4"
$vmhost = Get-VMHost -Name 192.168.3.205
$ds=Get-DataStore -Name datastore2
$linkedname = "{0}.linked" -f $vm.name
#Create the tempory VM
$linkedvm = New-VM -LinkedClone -Name $linkedName -VM $vm -ReferenceSnapshot $snapshot -VMHost $vmhost -Datastore $ds
#Create the Full VM
$newvm = New-VM -Name "fw.base" -VM $linkedvm -VMHost $vmhost -Datastore $ds
#A new Snap Shot
$newvm | new-snapshot -Name "Base"
#Cleanup the temporary linked clone
$linkedvm | Remove-VM
```
