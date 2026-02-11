#update module
Import-Module '480-utils' -Force
# show banner
480Banner
# get configuration
$conf = Get-480Config -config_path "480.json"
# connect to server
480Connect -server $conf.vcenter_server

#Write-Host "selecting your VM"
#Select-VM -folder "BASEVM"