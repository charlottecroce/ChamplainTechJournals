Reverse Shells

1. Login to sec335-rocky(10.0.17.200) from kali using ssh and your cyber.local credentials.
```
ssh charlotte.croce@10.0.17.200
```
2. Determine your IP address for your kali vm's eth0
3. On Kali, Create a nc listener on 4449/tcp
5. On Rocky Use a native bash reverse shell to connect back to your listener
6. Interact with sec335-rocky over your kali nc session.
