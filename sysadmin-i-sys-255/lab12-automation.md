---
description: >-
  In this lab, we set up the clone machines, configured SSH to use RSA keys as
  authentication, and used PSSH and Ansible to automate commands
---

# Lab12 - Automation

## Configure clone1, clone2, and clone3

For all three machines...

* Change network adapter to LAN
* `nmtui`
  * Manual IP address&#x20;
    * 10.0.5.70/24
    * 10.0.5.71/24
    * 10.0.5.72/24
  * Gateway 10.0.5.2
  * DNS 10.0.5.6 & 8.8.8.8
  * Search domain: nathan.local
* `systemctl restart network`
* `user add nathan && passwd nathan`
* `usermod -aG wheel nathan`
* Add DNS records to AD02

## Configuring SSH

### Creating RSA key pair for SSH

* `ssh-keygen`
  * Default location
  * enter a passphrase
* `ssh-copy-id nathan@clone2`
* `ssh-copy-id nathan@clone3`

<figure><img src="../.gitbook/assets/image (25).png" alt=""><figcaption></figcaption></figure>

### Add passwordless SSH login (for 1 hour)

* `` eval `ssh-agent` ``
* `ssh-add -t 1h`
* This is not permanent, you have to retype these commands every session

### Allow passwordless elevation to root by wheel group members

* On clone2 and clone3, uncomment this line in /etc/sudoers

<figure><img src="../.gitbook/assets/image (26).png" alt=""><figcaption></figcaption></figure>

## PSSH - Parallel SSH.&#x20;

* Allows you to run SSH commands on multiple hosts
*   On clone1

    * `yum install epel-release`
    * `yum install pssh`
    * create a text file called _ssh-hosts.txt_ and add IP addresses of clone2 and clone3

    <figure><img src="../.gitbook/assets/image (27).png" alt=""><figcaption></figcaption></figure>

    * make sure passwordless SSH is enabled
    * `pssh -i -h ssh-hosts.txt -- <command>`
      * `-i` - interactive - show command output

<figure><img src="../.gitbook/assets/image (28).png" alt=""><figcaption></figcaption></figure>

## install Ansible

*   On clone1

    * `sudo yum install ansible`
    * `ansible all -i ssh-hosts.txt -m ping`

    <figure><img src="../.gitbook/assets/image (29).png" alt=""><figcaption></figcaption></figure>

    * `-b` - tells Ansible that the user associated with the SSH public key at the other end of the connection is a sudoer user

<figure><img src="../.gitbook/assets/image (30).png" alt=""><figcaption></figcaption></figure>





