---
description: In this lab, we explored basic PowerShell scripting
---

# Lab10 - PowerShell

## AD Commands

* `Neq-ADUser -Name "Charlie" -SamAccountName "charlie" - AccountPassword(Read-Host -AsSecureString "Password: ") -Enabled $true`
* `Add-ADGroupMember -Identity "Sales-Users" - Members charlie`

<figure><img src="https://lh7-us.googleusercontent.com/yuCKKzJsbL2VJL5sVPcQIzLyQWuV2TMDL4CLXOJ-Q2nMhLBi6fkPr32FqvM3IN5obMTp2yBmL2xr09AfRQfUF93gZQp5nv9_84wZ0I5QWszJd4xIuA0AwHDKSEw988TywxU2Q1TBqo2UW03g-1l-MA" alt=""><figcaption></figcaption></figure>

## Allow PS Scripts to be Run

* `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`
* This allows current users to run local scripts and digitally signed remote scripts

## Remote Access

* `Enter-PSSession -ComputerName <computername>` - interactive remote session

<figure><img src="../.gitbook/assets/image (17).png" alt=""><figcaption></figcaption></figure>

* `Invoke-Command -ComputerName <computername> -ScriptBlock { <command> }` - launch a command remotely

<figure><img src="../.gitbook/assets/image (18).png" alt=""><figcaption></figcaption></figure>

* `Enable-PSRemoting` - allows remote commands to be executed on this machine
