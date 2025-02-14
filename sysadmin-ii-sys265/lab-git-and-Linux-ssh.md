# Git and Linux SSH

## docker-01
- `sudo apt install git`
- 'git clone https://github.com/charlottecroce/champlaintechjournals'
- `cd ~/champlaintechjournals/sysadmin-ii-sys265/configs/docker-01`
- 'sudo cp /etc/hosts .`
- `sudo cp /etc/netplan/* .`
- `sudo cp /etc/cloud/cloud.cfg .`
___
add ssh key
```
ssh-keygen -t rsa -b 4096 -C "sys265-docker01"
cat ~/.ssh/id_rsa
```
copy this to github ssh & gpg section
- `ssh -T git@github.com`
- git remote -v
  if git is using https. you will ahve to change it to ssh
  git remote set-url origin git@github.com:charlottecroce/champlaintechjournals
___
- `git add .`
- `git config user.email charlotte.croce@mymail.champlain.edu`
- `git config user.name charlottecroce`
- `git commit -m "added a readme"`
- `git push`


  # mgmt-01
- install git from web
- `git clone https://github.com/charlottecroce/champlaintechjournals`
- - `git config user.email charlotte.croce@mymail.champlain.edu`
- `git config user.name charlottecroce`
- cd ~/champlaintechjournals/sysadmin-ii-sys265/configs/mgmt-01
- `git commit -m "added a readme"`
- `git push`

create PAT and add creds in control panel
![image](https://github.com/user-attachments/assets/0f121ff2-21a4-44c1-9846-ab6e51d53ac2)

