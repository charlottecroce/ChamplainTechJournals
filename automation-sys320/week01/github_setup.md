# Basic GitHub commands
- Clone repo Using SSH: `git clone git@github.com:charlottecroce/SYS320.git`
- Clone repo Using HTPS: `git clone https://github.com/charlottecroce/SYS320.git`
- Add file to staging area: `git add <file>`
- Commit change: `git commit -m "commit message"`
- ID needed to commit: `git config --global user.name "charlottecroce"`
- ID needed to commit: `git config --global user.email "charlotte.croce@mymail.champlain.edu"`
- Push changes to repo: `git push`


# Ubuntu Setup
Install Git
- `apt-get update`
- `apt-get install git`

Create SSH key
- `sudu su`
- `ssh-keygen -t rsa -b 4096 -C "charlotte.croce@mymail.champlain.edu"`
- `ssh-add /root/.ssh/id_rsa`
- Check if SSH agent is running:`eval "$(ssh-agent -s)"`

Add key to GitHub account
- `cat /root/.ssh/id_rsa.pub` -> copy
- GitHub -> Settings -> SSH and GPG Keys -> New SSH Key -> Select Authentication Key
- Test Connection: `ssh -T git@github.com`

# Windows Setup
Install Git
- Download Git from https://git-scm.com/download/win
- I select nano as default editory


Windows Token Authentication
- When attempting a `git push` you will have an authentication window pop up. We will use token authentication
- Github - Settings - Developer Settings - Tokens(Classic) - Generate a personal access token
- Select the following fields in Scope: repo, write:packages, admin:org, admin:public_key, admin:repo_hook
- Control Panel -> Manage Windows Credentials -> Create Generic Credential -> add GitHub.com:username:password
- Copy the token into the field on the popup and you should be authenticated to push
