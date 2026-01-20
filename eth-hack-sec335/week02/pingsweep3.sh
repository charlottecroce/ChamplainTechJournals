#!/bin/sh
sudo nmap -sn 10.0.5.2-50 -oG sweep3.txt; grep -oE "([0-9]{1,3}\.){3}[0-9]{1,3}" sweep3.txt > sweep4.txt
