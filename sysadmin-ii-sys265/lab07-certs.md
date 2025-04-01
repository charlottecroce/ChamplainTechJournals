# Lab07 -certs

make certain -adm account is in the Enterprise Admins 
```powershell
Get-ADGroupMember "Enterprise Admins"
```
add RSAT to MGMT01. needs to run as administrator
```
Install-WindowsFeature RSAT-ADCS -IncludeManagementTools
```
Start remote PowerShell session
```
$session = New-PSSession -ComputerName ad01-charlotte
```
```
Invoke-Command -Session $session -ScriptBlock {
    # Install AD CS Role
    Install-WindowsFeature -Name AD-Certificate -IncludeManagementTools

    # Import the ADCS module
    Import-Module ADCSDeployment
}
```
```
Configure AD CS as an Enterprise Root CA remotely
Invoke-Command -Session $session -ScriptBlock {
    Install-AdcsCertificationAuthority `
        -CAType EnterpriseRootCA `
        -CryptoProviderName "RSA#Microsoft Software Key Storage Provider" `
        -KeyLength 4096 `
        -HashAlgorithmName SHA512 `
        -ValidityPeriod Years `
        -ValidityPeriodUnits 7 `
        -Force
}
```
```
Invoke-Command -Session $session -ScriptBlock {
    # create the shared folder for certs
    New-Item -Path "C:\Shares\Certs" -ItemType Directory -Force    
    New-SmbShare -Name "Certs" -Path "C:\Shares\Certs" -FullAccess "Domain Admins" -ChangeAccess "Authenticated Users"

    # copt cert to shared directory
    $cert = Get-ChildItem -Path "Cert:\LocalMachine\CA" | Where-Object {$_.Subject -like "*charlotte-ad01-CHARLOTTE-CA*"}
    
    # export cert to shared folder
    Export-Certificate -Cert $cert -FilePath "C:\Shares\Certs\charlotte-AD01-CHARLOTTE-CA.cer" -Type CERT
}
```



Install AD CS role with Certification Authority and Web Enrollment
```
Install-WindowsFeature -Name ADCS-Cert-Authority, ADCS-Web-Enrollment -IncludeManagementTools
```

Configure the Subordinate CA and generate certificate request
```
Install-AdcsCertificationAuthority `
    -CAType EnterpriseSubordinateCA `
    -CACommonName "mgmt01-CHARLOTTE-SubCA" `
    -CryptoProviderName "RSA#Microsoft Software Key Storage Provider" `
    -KeyLength 4096 `
    -HashAlgorithmName SHA512 `
    -OutputCertRequestFile "C:\SubCARequest.req"
```

Install the Web Enrollment service
```
Install-AdcsWebEnrollment
```

Move the certificate request to the Root CA, get it signed, and retrieve it
```
# Copy request to Root CA's shared folder
Copy-Item -Path "C:\SubCARequest.req" -Destination "\\ad01-charlotte\Certs\"

# Sign the request on the Root CA
Invoke-Command -Session $session -ScriptBlock {
    # Sign the subordinate CA certificate request
    certreq -submit -config "ad01-charlotte\charlotte-AD01-CHARLOTTE-CA" -attrib "CertificateTemplate:SubCA" "C:\Shares\Certs\SubCARequest.req" "C:\Shares\Certs\SubCACert.cer"
}

# Copy the signed certificate back to the Subordinate CA
Copy-Item -Path "\\ad01-charlotte\Certs\SubCACert.cer" -Destination "C:\"
```
```
# Start the CA service
Start-Service -Name CertSvc

# Install the issued certificate
certutil -installcert "C:\SubCACert.cer"

# Configure CA settings
certutil -setreg CA\CRLPeriodUnits 1
certutil -setreg CA\CRLPeriod "Weeks"
certutil -setreg CA\CRLOverlapPeriodUnits 12
certutil -setreg CA\CRLOverlapPeriod "Hours"

# Restart the service to apply changes
Restart-Service -Name CertSvc
```
```
# Verify the CA status
certutil -ping
```


Clean up the remote session
```
Remove-PSSession $session
```



open the CA console
  ```powershell
   certsrv.msc
   ```

### Create Certificate Template
- Expand root cert tree > RC Certificate Templates > Manage
- Duplicate User template
- General tab: Set name "Champ Lab User"
- Subject Name: Select "Build from AD info", uncheck all email options
- Extensions: Add "Smart Card Logon" to Application Policies
- Security: set "Authenticated Users" to Read, Enroll, Autoenroll permissions

## Issue Certificate Template
- in CA console
- Right-click Certificate Templates > New > Certificate Template to Issue > Select "Champ Lab User"

## Configure Group Policy
- gpmc.msc
- Create GPO "Champ Lab Users" at domain level
- Edit GPO > User Configuration > Policies > Windows Settings > Security Settings > Public Key Policies
- Enable "Certificate Services Client - Auto-Enrollment"
- Check both renewal options > OK

## Test Auto-Enrollment
- on WKS01:
- gpupdate /force
- Verify: gpresult /r
- certmgr.msc > Personal > Certificates > Verify "Champ Lab User" certificate is present

## Windows Admin Center Installation
- Download Windows Admin Center 2019 Evaluation
  - https://info.microsoft.com/ww-landing-windows-admin-center.html
  - download the msi
  - you will have to put in information. i just used fake info
- Express setup. Generate self-signed cert. Disable updates
- Logon via -adm account, add ad01 + wks10, install AD + DNS extensions, and uninstall Azure + Cluster extensions
