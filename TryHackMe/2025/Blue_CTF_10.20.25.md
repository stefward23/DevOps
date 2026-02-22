# Deploy & hack into a Windows machine, leveraging common misconfigurations issues.


## 1. Enumerate machine

First we did an nmap stealth scan to see what ports were open. We found 3 open ports under 1000.

<img width="550" height="164" alt="image" src="https://github.com/user-attachments/assets/839f137d-ca4a-40db-b95d-a39bf1b9446b" />

Secondly, we did another nmap scan and this time we saved the output to an .xml file. 

<img width="548" height="51" alt="image" src="https://github.com/user-attachments/assets/0c6466fc-b5dc-469e-81f4-5987dad16ce0" />

Then we tried to see which attack the machine was vulnerable to using searchsploit on the .xml file we created.
