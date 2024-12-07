---
description: >-
  In this lab, we installed and configured a WordPress site on a Windows 2019
  server
---

# Lab13 - WordPress on Windows

### MySQL

* go to https://dev.mysql/downloads/installer
* download the MSI file and run it
  * Full version, server mode, keep the rest defaults
* MySQL Workbench -> open the only connection

<figure><img src="../.gitbook/assets/image (35).png" alt=""><figcaption></figcaption></figure>

* Create a new scheme (database icon)

<figure><img src="../.gitbook/assets/image (37).png" alt=""><figcaption></figcaption></figure>

* Add all privileges to root

<figure><img src="../.gitbook/assets/image (38).png" alt=""><figcaption></figcaption></figure>

### PHP

* go to https://windows.php.net/download
* download the non thread safe zip

<figure><img src="../.gitbook/assets/image (32).png" alt=""><figcaption></figcaption></figure>

* extract as `php` into the Program Files folder
* go to Environment Variables and add php to PATH

<figure><img src="../.gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>



* In the php folder, rename php.ini-production to php.ini
* edit php.ini
  * cgi.force\_redirect = 0
  * cgi.fix\_pathinfo = 1
  * fastcgi.impersonate = 1
  * fastcgi.logging = 0
  * extension\_dir = "ext"
  * extension=mysqli
  * extension=pdo\_mysql

### Install PHPMyAdmin

* go to phpmyadmin.net
* download the zip on the top right of the page

### C++ and URL Rewrite

* download from Microsoft and run the installer

### Internet Information Services (IIS)

* Add Web Server (IIS) feature

<figure><img src="../.gitbook/assets/image (33).png" alt=""><figcaption></figcaption></figure>

* no roles needed
*   Web Server Roles

    * Custom Logging & Logging Tools&#x20;
    * CGI
    * IIS 6 Management Compatibility & IIS Management Scripts and Tools
    * ASP.NET 4.7 (latest version)

    <figure><img src="../.gitbook/assets/image (34).png" alt=""><figcaption></figcaption></figure>


* Go to http://localhost to check if IIS is running
* Tools -> Internet Information Services (IIS) Manager
* Handler Mappings
* Add Module Mapping...

<figure><img src="../.gitbook/assets/image (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>

* IIS Manager -> default documents -> add index.php to top priority
* IIS Manager -> FastCGI Settings -> Environment Variables

<figure><img src="../.gitbook/assets/image (3) (1).png" alt=""><figcaption></figcaption></figure>

* IIS Manager -> Application Pools -> Add Application pool... -> name it Wordpress (keep defaults)
* rc Wordpress -> Set Application Pool Defaults -> Application Pool Identity
* Sites -> Default Web Site -> Basic Settings...

<figure><img src="../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

### Install WordPress!!!!

* download zip from website
* extract into C:\inetpub\wwwroot
* rename to just wordpress
* copy paste all files to the root wordpress folder, then delete the internal wordpress folder
* rename wp-config-sample.php to wp-config.php
* edit with notepad

<figure><img src="../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

