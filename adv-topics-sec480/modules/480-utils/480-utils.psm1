function Install-PowerCLI(){
    if(Get-Module VMware.PowerCLI -ListAvailable){
        Write-Host "PowerCLI Module already installed"
    }else{
        Install-Module VMware.PowerCLI -Scope CurrentUser
        Set-PowerCLIConfiguration -InvalidCertificateAction Ignore
        Set-PowerCLIConfiguration -Scope User -ParticipateInCEIP $false  
    }
}

function 480Banner(){
    Write-Host "hello sec480!"
}

function 480Connect([string] $server){

    $conn = $global:DefaultVIerver
    if ($conn){
        $msg = "already connected to: {0}" -f $conn
        Write-Host -ForegroundColor Green $msg
    }else{
        $conn = Connect-VIServer -Server $server
        #if this fails, let Connect-VIServer handles errors
    }

}

Function Get-480Config([string] $config_path)
{
    Write-Host "Reading " $config_path
    $conf=$null
    if(Test-Path $config_path){
        $conf = (Get-Content -Raw -Path $config_path | ConvertFrom-Json)
        $msg = "using configuration at {0}" -f $config_path
        Write-Host -ForegroundColor Green $msg
    }else{
        Write-Host -ForegroundColor Yellow "No Configuration"
    }
    return $conf
}


Function Select-VM([string] $folder){
    $selected_vm=$null
    try{
        $vms = Get-VM -Location $folder
        $index = 1
        foreach($vm in $vms){
            Write-Host [$index] $vm.name
            $index+=1;
        }
        $pick_index = Read-Host "select an index number [x]"
        #TODO: errror handling invalid input
        $selected_vm = $vms[$pick_index - 1]
        Write-Host "you selected: " $selected_vm.name

        # return entire vm object, not just name
        return $selected_vm
    }catch{
        Write-Host -ForegroundColor Red "Invalid folder: $folder"
    }
}


Function New-VMLinkedClone(){
    $conf = Get-480Config -config_path "480.json"
    #Source VM
    $vm = Select-VM($conf.vm_folder)
    $snapshot = Get-Snapshot -VM $vm -Name "Base"
    $vmhost = Get-VMHost -Name $conf.esxi_host
    $ds = Get-DataStore -Name $conf.default_datastore
    $linkedname = "{0}.linked" -f $vm.name
    #Create the tempory VM
    $linkedvm = New-VM -LinkedClone -Name $linkedName -VM $vm -ReferenceSnapshot $snapshot -VMHost $vmhost -Datastore $ds
    # A new Snap Shot
    $linkedvm | new-snapshot -Name "Base"
    return $linkedvm
}

Function New-VMClone(){
    $conf = Get-480Config -config_path "480.json"
    #Source VM
    $vm = Select-VM($conf.vm_folder)
    $snapshot = Get-Snapshot -VM $vm -Name "Base"
    $vmhost = Get-VMHost -Name $conf.esxi_host
    $ds = Get-DataStore -Name $conf.default_datastore
    $linkedname = "{0}.linked" -f $vm.name
    #Create the tempory VM
    $linkedvm = New-VM -LinkedClone -Name $linkedName -VM $vm -ReferenceSnapshot $snapshot -VMHost $vmhost -Datastore $ds

    #Create the Full VM
    $clonedvmname = $linkedvm.name.Replace(".linked", ".clone").ToString()
    $newvm = New-VM -Name $clonedvmname -VM $linkedvm -VMHost $vmhost -Datastore $ds
    #A new Snap Shot
    $newvm | new-snapshot -Name "Base"
    #Cleanup the temporary linked clone
    $linkedvm | Remove-VM
}
