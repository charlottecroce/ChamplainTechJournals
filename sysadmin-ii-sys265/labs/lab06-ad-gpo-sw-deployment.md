# AD Group Policy & SW Deployment


## Prepare an OU, user & workstation
Before we get into configuring a Group Policy Object (GPO) within Active Directory (AD), let’s set the AD stage to deploy a software package. Via AD Users & Computers, create a “Test OU”.

![image](https://github.com/user-attachments/assets/a5a9d811-0e27-48e2-b25d-97cb9e345e56)

Use Powershell on AD01 via MGMT01 to create another OU called “Software Deploy”, move WKS01 and your regular named account into it, and then delete the Test OU.
```powershell
# Create another OU called Software Deploy under charlotte.local
# Move WKS01 and your regular named account into it, and then
# Delete the Test OU 

# Get the domain Distinguished Name (DN)
$domainDN = (Get-ADDomain).DistinguishedName

# Create the "Software Deploy" OU
$swDeployOUDN = "OU=Software Deploy,$domainDN"
$swDeployOU = Get-ADOrganizationalUnit -Identity $swDeployOUDN
if($swDeployOU){
    Write-Host "'Software Deploy' OU already exists at $swDeployOUDN"
}else{
    New-ADOrganizationalUnit -Name "Software Deploy" -Path $domainDN -Description "Software Deployment OU"
    Write-Host "Created $swDeployOUDN"
}

# Move WKS01 computer to new OU
$computerDN = (Get-ADComputer -Identity "WKS01-CHARLOTTE").DistinguishedName
$targetOUDN = "OU=Software Deploy,$domainDN"
Move-ADObject -Identity $computerDN -TargetPath $targetOUDN
Write-Host "Computer $computerDN added to $targetOUDN"

# Move charlotte.croce-adm to new OU
$userDN = (Get-ADUser -Identity "charlotte.croce-adm").DistinguishedName
Move-ADObject -Identity $userDN -TargetPath $targetOUDN
Write-Host "User $userDN added to $targetOUDN"

# Remove the "Protect from accidental deletion" flag from Test OU and delete
$testOU = Get-ADOrganizationalUnit -Filter {Name -eq "Test OU"}
if($testOU){
    Set-ADObject -Identity $testOU -ProtectedFromAccidentalDeletion $false
    Remove-ADOrganizationalUnit -Identity $testOU -Confirm:$false
    Write-Host "Deleted $testOU"
}
```

## Deploying Software via GPO

- On MGMT01, download the current Putty x64-bit Windows Installer Package.
- Next, create a Share on MGMT01 named ‘Software’ and place Putty’s .msi in it, so users and computers (via GPO) can access & install it shortly.
  - see SYS255 file share docs [here](https://github.com/charlottecroce/ChamplainTechJournals/blob/main/sysadmin-i-sys255/lab07-lab-server-core-and-remote-administrator-tools.md#use-rsat-to-add-to-fs01-and-create-a-sales-users-share). No need to map drive to letter
- Via Group Policy Management feature on MGMT (You need to install this), create a new GPO named ‘Deploy SW’ within the Software Deploy OU. \
![image](https://github.com/user-attachments/assets/64d738b7-1b8e-45ea-9f7d-474fc6679cfb)
![image](https://github.com/user-attachments/assets/dccadcee-10f4-4fce-ac7b-0f7b9b87f0cd)
- Edit the new GPO by creating a new Software installation, and assign Putty’s .msi package to deploy. \
![image](https://github.com/user-attachments/assets/45ad5e35-665c-4861-a8be-e9aa17d6b676)
- With the new GPO setting, run `gpupdate /force` on WKS01, and then allow the restart when prompted. PuTTY should now be installed

> [!Note]
> An extremely common issue you’ll encounter in MS Window environments are the differences between Local Permissions vs. Share Permissions: 
>
> Local Permissions (also called NTFS Permissions): Permissions that are applied only Locally (and not Remotely) on the OS, and affects both Local (i.e. via keyboard) and Remote (i.e. via network) account access.
>
> Share Permissions: Permissions that are applied only Remotely (and not Locally) to the OS, and affects only Remote (i.e. via network shares) account access.
>
> If both Shared & Local Permissions are set, then MOST RESTRICTIVE PERMISSION WINS. #LeastPriledgeRules -- summary [here](https://blog.netwrix.com/ntfs-vs-share-permissions)


