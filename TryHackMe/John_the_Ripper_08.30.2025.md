

### URL: https://tryhackme.com/room/johntheripperbasics

#### Word list repo: https://github.com/danielmiessler/SecLists

##### John Basic Syntax
The basic syntax of John the Ripper commands is as follows. We will cover the specific options and modifiers used as we use them.

john [options] [file path]

john: Invokes the John the Ripper program
[options]: Specifies the options you want to use
[file path]: The file containing the hash you’re trying to crack; if it’s in the same directory, you won’t need to name a path, just the file.

Identifying Hashes, John automatically detects the hash being used. Sometimes it doesnt play nice.

Tools to assist: https://gitlab.com/kalilinux/packages/hash-identifier/-/tree/kali/master and https://hashes.com/en/tools/hash_identifier

Good sites: https://gitlab.com/kalilinux

Microsoft: In Windows, SAM (Security Account Manager) is used to store user account information, including usernames and hashed passwords. You can acquire NTHash/NTLM hashes by dumping the SAM database on a Windows machine, using a tool like Mimikatz,In Windows, SAM (Security Account Manager) is used to store user account information, including usernames and hashed passwords. You can acquire NTHash/NTLM hashes by dumping the SAM database on a Windows machine, using a tool like Mimikatz,
