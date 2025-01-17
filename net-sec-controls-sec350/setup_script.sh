#!/bin/bash
# script to streamline basic linux setup


function sethostname(){
    if [ -z "$1" ]; then # if no arg (using menu), prompt user
    	echo "current hostname: " $(hostname)
	    echo -n "new hostname (<ENTER> to skip): "
	    read newhostname
        if [ -z ${newhostname} ]; then
            return 0
        fi
	    echo "...'hostnamectl set-hostname ${newhostname}'"
        hostnamectl set-hostname ${newhostname}
    else # if arg provided, set hostname to arg
        hostnamectl set-hostname $1
    fi
	echo "current hostname: " $(hostname)
}

function addsudouser(){
    if [ -z $2 ]; then
        echo -n "username: "
        read username
        echo -n "password: "
        read password
        echo "...adduser ${username}"
        adduser ${username}
        echo "...echo ${password} | passwd ${username} --stdin"
        echo ${password} | passwd ${username} --stdin
        echo "...'usermod -aG sudo ${username}"
        usermod -aG sudo ${username}
    fi
}

# privilege check. this script has to be run as root (sudo)
user=$(whoami)
if [[ "$user" != "root" ]]; then
	echo "please run as root. exiting..."
	exit 0
fi

# interactive menu
while :
do
	echo "PLease select an option:"
	echo "[1] Set Hostname"
	echo "[2] create user"
	echo "[7] Quit"
    echo -n "> "
	read userInput
	echo ""

	if [[ "$userInput" == "1" ]]; then
		sethostname

	elif [[ "$userInput" == "2" ]]; then
		addsudouser

	elif [[ "$userInput" == "7" ]]; then
		echo "Exiting,,."
		break
	fi
done

