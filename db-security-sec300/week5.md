# Week5
Emailing failed login attempts

- create App password at: https://security.google.com/settings/security/apppasswordsLinks to an external site. 
- install ssmtp
  - `sudo apt-get update && sudo apt-get install ssmtp`

- edit `/etc/ssmtp/ssmtp.conf`
```
root=charlotte.croce@mymail,champlain.edu
mailhub=smtp.gmail.com:587
AuthUser=charlotte.croce@mymail.champlain.edu
AuthPass=YourAuthPass
UseSTARTTLS=Yes
```


- Testing email functionality
```
echo "To: charlotte.croce@mymail,champlain.edu" > emailform.txt
echo "Subject: Database Incident" >> emailform.txt
echo "Incident of Database" >> emailform.txt
cat emailform.txt | ssmtp charlotte.croce@mymail,champlain.edu
```

- Script to send email with failed login attempts

![image](https://github.com/user-attachments/assets/9587f614-c944-4943-9d33-aedb0e477008)

crontab
- add permissions so crontab can execute the script
  - `chmod +x dbsec.bash`
- `crontab -l` : list scheduled tasks
- `crontab -e` : edit scheduled tasks
- run the script every day at 3:35pm
  - `35 15 * * * /bin/bash -c "/root/dbsec.bash"`

