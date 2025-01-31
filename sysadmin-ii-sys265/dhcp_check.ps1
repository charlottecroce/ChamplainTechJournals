# SYS265 - DHCP Lab
# 1/31/25

# Get Username
function get_username(){
    Write-Host 'Username:'$env:USERNAME
}

# Get IP Address
function get_ip(){
    $ip_address = (Get-NetIPAddress -AddressFamily IPv4 | Select IPv4Address | Where-Object { $_.IPv4Address -ne "127.0.0.1" } | Format-Table -HideTableHeaders | Out-String).Trim()
    Write-Host 'IP Address:'$ip_address
}

# Get DHCP Server Address
function get_dhcp(){
    $dhcp_address = (Get-CimInstance Win32_NetworkAdapterConfiguration | Select DHCPServer | Format-Table -HideTableHeaders | Out-String).Trim()
    Write-Host 'DHCP Server:'$dhcp_address
    $dhcp_lease = (Get-CimInstance Win32_NetworkAdapterConfiguration | Select DHCPLeaseExpires | Format-Table -HideTableHeaders | Out-String).Trim()
    Write-Host 'Lease Expiration:'$dhcp_lease
}

# Get Gateway IP
function get_gateway(){
    $gateway_address = (Get-CimInstance Win32_NetworkAdapterConfiguration | Select DefaultIPGateway | Format-Table -HideTableHeaders | Out-String).Trim()
    Write-Host 'Default Gateway:'$gateway_address
}

# Get DNS Server IP
function get_dns(){
    $dns_address = ((Get-DnsClientServerAddress -AddressFamily IPv4 | Where-Object { $_.InterfaceAlias -ne "loopback" }).ServerAddresses | Out-String).Trim()
    Write-Host 'DNS Server:'$dns_address
}


clear

$Prompt = "`nChoose number for operation`n"
$Prompt += "1. All`n"
$Prompt += "2. Username`n"
$Prompt += "3. IP`n"
$Prompt += "4. DHCP`n"
$Prompt += "5. Default Gateway`n"
$Prompt += "6. DNS`n"
$Prompt += "7. exit"

$operation = $true

while($operation){
    Write-Host $Prompt | Out-String
    $choice = Read-Host 
    Write-Host "----------"

    if($choice -eq 1){
        get_username
        get_ip
        get_dhcp
        get_gateway
        get_dns
    }

    elseif($choice -eq 2){
        get_username
    }


    elseif($choice -eq 3){
        get_ip
    }


    elseif($choice -eq 4){
        get_dhcp
    }

    elseif($choice -eq 5){
        get_gateway
    }

    elseif($choice -eq 6){
        get_dns
    }

    elseif($choice -eq 7){
        Write-Host "Goodbye" | Out-String
        exit
        $operation = $false
    }

    else{
        Write-Host "Invalid Input" | Out-String
    }
    
    Write-Host "----------"

}

