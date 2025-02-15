# secure-ssh.sh
# author: charlottecroce
#
# creates a new SSH user using $1 parameter
# adds a public key from the local repo or curled from the remote repo
# removes roots ability to SSH in
#
#
# Requirements:
#	must run as root
#	$1 = username of new user
#

# check if script is run as root
if [ $EUID -ne 0 ]; then
    echo "run as root"
    exit 1
fi

# check if username was provided
if [ -z $1 ]; then
    echo "Usage: $0 <username>"
    exit 1
fi

# vars
USERNAME=$1
AUTHORIZED_KEYS_DIR="/home/$USERNAME/.ssh"
AUTHORIZED_KEYS_FILE="$AUTHORIZED_KEYS_DIR/authorized_keys"

# create user
useradd -m -d /home/$USERNAME -s /bin/bash $USERNAME
echo "user: <$USERNAME> created"

# create .ssh directory, give perms to user
mkdir -p $AUTHORIZED_KEYS_DIR
chmod 700 $AUTHORIZED_KEYS_DIR

# try to get SSH pubkey from local repo
if [ -f "~/champlaintechjournals/sysadmin-ii-sys265/linux/public-keys/id_rsa.pub" ]; then
    echo "key found in local repo"
else
    # if local key doesn't exist, get from github repo...
    echo "no key found in local repo, cloning from github..."
    git clone https://github.com/charlottecroce/champlaintechjournals ~/
    echo "retreived key from github repo"
fi

cat ~/champlaintechjournals/sysadmin-ii-sys265/linux/public-keys/id_rsa.pub >> $AUTHORIZED_KEYS_FILE
echo "added key to $AUTHORIZED_KEYS_FILE"

# set perms, set new user as directory owner
chmod 600 $AUTHORIZED_KEYS_FILE
chown -R $USERNAME:$USERNAME $AUTHORIZED_KEYS_DIR

# disable root SSH login
sed -i 's/PermitRootLogin.*/PermitRootLogin no/' /etc/ssh/sshd_config
echo "Root SSH access has been disabled"

# disable password authentication
sed -i 's/PasswordAuthentication.*/PasswordAuthentication no/' /etc/ssh/sshd_config
echo "Password authentication has been disabled"

# Restart SSH service
echo "restarting ssh..."
systemctl restart sshd

echo "complete!"

