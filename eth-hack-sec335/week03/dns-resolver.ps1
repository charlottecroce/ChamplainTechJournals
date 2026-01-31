
param (
    [string]$Network,
    [string]$DnsServer
)

$results = for ($i = 1; $i -le 254; $i++) {
    $ip = "$Network.$i"

    $record = Resolve-DnsName -DnsOnly $ip -Server $DnsServer -ErrorAction Ignore

    if($record){
        [PSCustomObject]@{
            IPAddress = $ip
            Hostname  = $record.NameHost
        }
    }
}

$results
