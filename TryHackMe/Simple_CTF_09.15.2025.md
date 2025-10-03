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
<img width="992" height="389" alt="Screenshot 2025-10-03 070541" src="https://github.com/user-attachments/assets/ca54e257-52b9-4570-b9dc-e3585d96f17f" />
Accessed the path:
<img width="966" height="553" alt="Screenshot 2025-10-03 070541" src="https://github.com/user-attachments/assets/3a92a49c-1950-4feb-a6a4-088ea886c860" />

The site is powered by CMS Made Simple version 2.2.8

# EXPLOIT DB
A google search for exploits on this service leads us to this: https://www.exploit-db.com/

We downloaded the exploit from that website and attempted to expoit it but received errors about the url not being found.

We decided to use an updated version from: https://github.com/Dh4nuJ4/SimpleCTF-UpdatedExploit

Which worked:
<img width="729" height="150" alt="image" src="https://github.com/user-attachments/assets/82f3e3c6-7fc4-4ba3-8ffc-06c35f064378" />

The credentials worked logging into the /simple/admin path.

# SSH

Tried the same credentials: ssh -p 2222 mitch@ip.address
Which worked.
 
# VIM
The next question was, What can you leverage to spawn a privileged shell?

It was a 3 letter word, we guessed. VIM
<img width="231" height="61" alt="image" src="https://github.com/user-attachments/assets/b66a44be-d5db-4afa-baf7-3f541559a4c5" />

Researched how to leverage vim to spawn a privileged shell.

We both took different directions.

# Bobby


# Dope

Youtube on VIM Privilge Escalation Linux: https://www.youtube.com/watch?v=hYQVRDfA5yE

It should us how to openssl to create a hashed password and sudo vim into /etc/passwd and add a root user to it.
<img width="589" height="175" alt="image" src="https://github.com/user-attachments/assets/b0549c6c-d0f6-4c0b-8e59-40510f094ebb" 

After going over bobbys solution, we noticed that Dope's solution only worked because the user had the ability to run vim as a sudo user. If he did not have su vim privlige, saving the /etc/passwd would have failed.

Good Command to not: sudo -l -l
<img width="810" height="279" alt="image" src="https://github.com/user-attachments/assets/6911c552-1772-4ff5-a1c5-baa6a9434981" />

Notably other write-ups: 
1. https://sckull.github.io/posts/simplectfthm/
2. https://bobloblaw321.wixsite.com/website/post/tryhackme-simplyctf

# COMPLETED: 2025-10-1
