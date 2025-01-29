# DevOps Time: 5 hrs

### Stefan:

# Configured raspberry pi 3: 

### Check OS model

```
cat /etc/os-release
```
**output:**

PRETTY_NAME="Raspbian GNU/Linux 10 (buster)"
NAME="Raspbian GNU/Linux"
VERSION_ID="10"
VERSION="10 (buster)"
VERSION_CODENAME=buster
ID=raspbian
ID_LIKE=debian
HOME_URL="http://www.raspbian.org/"
SUPPORT_URL="http://www.raspbian.org/RaspbianForums"
BUG_REPORT_URL="http://www.raspbian.org/RaspbianBugs"

# Filesystem:

### Check Disk volumes

```
df -h
```

Filesystem      Size  Used Avail Use% Mounted on
/dev/root        29G  4.1G   24G  15% /
devtmpfs        430M     0  430M   0% /dev
tmpfs           462M     0  462M   0% /dev/shm
tmpfs           462M   13M  450M   3% /run
tmpfs           5.0M  4.0K  5.0M   1% /run/lock
tmpfs           462M     0  462M   0% /sys/fs/cgroup
/dev/mmcblk0p1  253M   49M  204M  20% /boot
tmpfs            93M  4.0K   93M   1% /run/user/100

### Configured for DNS: https://www.noip.com/
### DDNS: mypc.webhop.me

Successfully enabled port forwarding on port 22
![image](https://github.com/user-attachments/assets/b029d0da-3795-420a-8eb4-ce4ce23ed91a)

### Akeem:

Configured Mint OS: 
```
cat /etc/os-release
```
**output:**

NAME="Linux Mint"
VERSION="21.3 (Virginia)"
ID=linuxmint
ID_LIKE="ubuntu debian"
PRETTY_NAME="Linux Mint 21.3"
VERSION_ID="21.3"
HOME_URL="https://www.linuxmint.com/"
SUPPORT_URL="https://forums.linuxmint.com/"
BUG_REPORT_URL="http://linuxmint-troubleshooting-guide.readthedocs.io/en/latest/"
PRIVACY_POLICY_URL="https://www.linuxmint.com/"
VERSION_CODENAME=virginia
UBUNTU_CODENAME=jammy

# Filesystem:

```
df -h
```

Filesystem      Size  Used Avail Use% Mounted on
tmpfs           1.6G  1.8M  1.6G   1% /run
/dev/sda3       916G  155G  715G  18% /
tmpfs           7.8G  192K  7.8G   1% /dev/shm
tmpfs           5.0M  4.0K  5.0M   1% /run/lock
tmpfs           7.8G  216K  7.8G   1% /run/qemu
/dev/sda2       512M   34M  479M   7% /boot/efi
tmpfs           1.6G  160K  1.6G   1% /run/user/1000

Installed wireguard: 
https://www.instructables.com/Wireguard-VPN-Server-Linux-Ubuntu-Mint-How-To/

Enabled port forwarding:

Attempted to ssh from a remote location and was unsuccessful

Ensured the firewall on Mint OS server allowed incoming SSH connections:
Command: sudo ufw status
![image](https://github.com/user-attachments/assets/d6c5503d-a381-48b8-aa27-06c4e3454466)

 

Ensured the ip on Mint OS server allowed incoming SSH connections:
Command: sudo iptables -L -n | grep 22
![image](https://github.com/user-attachments/assets/10c1cbee-d1e4-4f1f-b119-cd11b20ad13e)

Retried using a different server

Configured Ubuntu-Server VM:

```
cat /etc/os-release
```

![image](https://github.com/user-attachments/assets/d6c37ba4-9866-4056-804f-3a24b4da1abd)


# Filesystem:

```
 df -h
```

![image](https://github.com/user-attachments/assets/74bc7a0a-483b-4285-8179-1e71bb111ee6)

 
DDNS: https://www.noip.com/
DDNS: techd.ddnsking.com

Successfully enabled port forwarding on port 22
