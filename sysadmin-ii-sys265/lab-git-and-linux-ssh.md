# Git and Linux SSH

>[!Note]
>This entry is pretty empty because I've already written [this journal Entry for using git/github](https://github.com/charlottecroce/ChamplainTechJournals/blob/main/automation-sys320/week01/github_setup.md)

# Automating ssh authentication
- generate SSH key pair on your management node (in this case, web-01)
- push pubkey to github repo
- run the secure-ssh.sh script on remote host to create a new user that has the pubkey in `.../.ssh/authorized_keys`
- you can now ssh from web-01 to remote hosts without password!

___
## docker-01
```
sudo apt install git
git clone https://github.com/charlottecroce/champlaintechjournals
cd ~/champlaintechjournals/sysadmin-ii-sys265/configs/docker-01
sudo cp /etc/hosts .
sudo cp /etc/netplan/* .
sudo cp /etc/cloud/cloud.cfg .
```
___
add ssh key
```
ssh-keygen -t rsa -b 4096 -C "sys265-docker01"
cat ~/.ssh/id_rsa
```
copy this to github ssh & gpg section
- to test: `ssh -T git@github.com`
- `git remote -v`
  - if git is using https. you will ahve to change it to ssh
  - `git remote set-url origin git@github.com:charlottecroce/champlaintechjournals`
___
- `git add .`
- `git config user.email charlotte.croce@mymail.champlain.edu`
- `git config user.name charlottecroce`
- `git commit -m "added a readme"`
- `git push`

  # mgmt-01
- install git from web
- `git clone https://github.com/charlottecroce/champlaintechjournals`
- `git config user.email charlotte.croce@mymail.champlain.edu`
- `git config user.name charlottecroce`
- `cd ~/champlaintechjournals/sysadmin-ii-sys265/configs/mgmt-01`
- `git commit -m "added a readme"`
- `git push`
- login with token

# web-01
- `sudo yum install git`
- create ssh key and connect to git with it
- `mkdir -p linux/public-keys`
- `mkdir -p linux/ubuntu`
- `mkdir -p linux/centos7`
- create [secure-ssh.sh script](https://github.com/charlottecroce/ChamplainTechJournals/blob/main/sysadmin-ii-sys265/linux/centos7/secure-ssh.sh)
