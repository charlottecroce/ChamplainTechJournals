---
description: >-
  In this lab, we installed and configured a WordPress site on a Windows 2019
  server
---

# Lab13 - WordPress on Windows Server

### MySQL

* go to https://dev.mysql/downloads/installer
* download the MSI file and run it
  * Full version, server mode, keep the rest defaults
* MySQL Workbench -> open the only connection

<figure><img src=".gitbook/assets/image (35).png" alt=""><figcaption></figcaption></figure>

* Create a new scheme (database icon)

<figure><img src=".gitbook/assets/image (37).png" alt=""><figcaption></figcaption></figure>

* Add all privileges to root

<figure><img src=".gitbook/assets/image (38).png" alt=""><figcaption></figcaption></figure>

### Install PHP

* go to https://windows.php.net/download
* download the non thread safe zip

<figure><img src=".gitbook/assets/image (32).png" alt=""><figcaption></figcaption></figure>

* extract as `php` into the Program Files folder
* go to Environment Variables and add php to PATH

<figure><img src=".gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>

<figure><img src=".gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>



* In the php folder, rename php.ini-production to php.ini
* edit php.ini
  * cgi.force\_redirect = 0
  * cgi.fix\_pathinfo = 1
  * fastcgi.impersonate = 1
  * fastcgi.logging = 0
  * extension=mysqli
  * extension=pdo\_mysql



### Install phpmyadmin

* go to phpmyadmin.net
* download the zip on the top right of the page

### Install C++ from Microsoft

### Internet Information Services (IIS)

* Add Web Server (IIS) feature

<figure><img src=".gitbook/assets/image (33).png" alt=""><figcaption></figcaption></figure>

* no roles needed
*   Web Server Roles

    * Custom Logging & Logging Tools&#x20;
    * CGI
    * IIS 6 Management Compatibility & IIS Management Scripts and Tools
    * ASP.NET 4.7 (latest version)

    <figure><img src=".gitbook/assets/image (34).png" alt=""><figcaption></figcaption></figure>


* Go to http://localhost to check if IIS is running
* Tools -> Internet Information Services (IIS) Manager
*



