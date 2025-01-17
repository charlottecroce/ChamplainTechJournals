#!/bin/bash

function sethostname(){
	echo "current hostname: " $(hostname)
	echo "new hostname (q to exit): "
	read newHostname
	echo "executing...'hostnamectl set-hostname " $(newHostname)"'"
	hostnamectl set-hostname newhostname
	echo "hostname: " $(hostname)
}


user=$(whoami)
if [[ "$user" != "root" ]]; then
	echo "please run as root. exiting..."
	exit 0

while :
do
	echo "PLease select an option:"
	echo "[1] Set Hostname"
	echo "[2] Set IP"
	echo "[7] Quit"

	read userInput
	echo ""

	if [[ "$userInput" == "1" ]]; then
		sethostname

	elif [[ "$userInput" == "2" ]]; then
		echo "IP:"

	elif [[ "$userInput" == "7" ]]; then
		echo "Exiting,,."
		break
	fi
done
