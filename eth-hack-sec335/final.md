
# bree

## nslookup
```
└─$ nslookup bree.shire.org 10.0.5.22 
Server:         10.0.5.22
Address:        10.0.5.22#53

Name:   bree.shire.org
Address: 10.0.5.32
```
ip address: 10.0.5.32

## nmap scan
```
└─$ sudo nmap -sS -sV 10.0.5.32 -p-
Starting Nmap 7.95 ( https://nmap.org ) at 2026-04-14 10:16 EDT
Nmap scan report for 10.0.5.32
Host is up (0.00084s latency).
Not shown: 65533 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.7 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 10.44 seconds
```

## dirb
```
└─$ dirb http://10.0.5.32

-----------------
DIRB v2.22    
By The Dark Raver
-----------------

START_TIME: Tue Apr 14 10:20:03 2026
URL_BASE: http://10.0.5.32/
WORDLIST_FILES: /usr/share/dirb/wordlists/common.txt

-----------------

GENERATED WORDS: 4612                                                          

---- Scanning URL: http://10.0.5.32/ ----
==> DIRECTORY: http://10.0.5.32/addons/                                                    
==> DIRECTORY: http://10.0.5.32/assets/                                                    
+ http://10.0.5.32/cp (CODE:200|SIZE:631)                                                  
+ http://10.0.5.32/favicon.ico (CODE:200|SIZE:82726)                                       
+ http://10.0.5.32/index.php (CODE:302|SIZE:0)                                             
==> DIRECTORY: http://10.0.5.32/install/                                                   
==> DIRECTORY: http://10.0.5.32/lib/                                                       
==> DIRECTORY: http://10.0.5.32/modules/                                                   
+ http://10.0.5.32/server-status (CODE:403|SIZE:274)                                       
==> DIRECTORY: http://10.0.5.32/storage/                                                   
==> DIRECTORY: http://10.0.5.32/vendor/                                                    
              
-----------------
END_TIME: Tue Apr 14 10:20:11 2026
DOWNLOADED: 9224 - FOUND: 5
```

<img width="519" height="374" alt="image" src="https://github.com/user-attachments/assets/55a54077-cc39-43b9-81fc-afb0b619bccf" />


found at http://10.0.5.32/cp
```
#!/usr/bin/env php
<?php

if (PHP_SAPI !== 'cli') {
    exit('Script needs to be run from Command Line Interface (cli)');
}

if (!defined('COCKPIT_CLI')) define('COCKPIT_CLI', true);

include_once(__DIR__."/bootstrap.php");

if (isset($argv[1])) {

    $cmd = str_replace('../', '', $argv[1]);

    switch($cmd) {

        case 'test':
            CLI::writeln("Yepp!", true);
            break;
        default:

            if ($script = cockpit()->path("#config:cli/{$cmd}.php")) {
                include($script);
            } else {
                CLI::writeln("Command - {$cmd} - not found!", false);
            }
    }
}
```

