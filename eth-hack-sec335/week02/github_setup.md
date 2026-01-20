to generate key:

passphrase 335335
```
ssh-keygen -t ed25519 -C "charlotte.croce@mymail.champlain.edu"
eval "$(ssh-agent -s)"
ssh-add /root/.ssh/id_ed25519
cat /root/.ssh/id_ed25519.pub
```


then add key to github settings, clone repo, and now you're ready to commit to repo
