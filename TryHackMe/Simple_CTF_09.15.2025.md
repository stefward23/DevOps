# Simple CTF: "Beginner level ctf"

## https://tryhackme.com/room/easyctf

## Connect Kali VM to openvpn
```
sudo openvpn "filename.ovpn"
```

### OS used:
Linux: Debian Based
### Tools used: 
# NMAP
Used to find services running on ports
<img width="952" height="741" alt="image" src="https://github.com/user-attachments/assets/2600b531-8eb3-4dae-8818-30c77444383f" />

# TELNET + FTP
We used telnet to connect to the FTP port site, we did not notice that to login we just needed to enter the user anonymous without a password. 
Which we could then have probed and found a hint
<img width="912" height="625" alt="image" src="https://github.com/user-attachments/assets/d7ef9f38-a89e-4ec5-9a85-83e6c1732fc8" />

# HTTP

Used firebox to access the webserver running on port 80

gobuster to find / paths of web application hosted on port 80. i.e /simple /admin etc

# GOBUSTER
We spent a few hours trying to find why a webserver was running on the system and just had the default page.
Attempted to use tools like nikto to no success. 

Researched and used AI to find a tool for the job.

It revealed that the path /simple was accessible 

