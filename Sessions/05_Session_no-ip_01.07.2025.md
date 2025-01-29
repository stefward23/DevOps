# Added Dynamic Update Client DUC to macpi & beastubuntu 2hrs
## Raspberry Pi 3B+ Commands
```
wget --content-disposition https://www.noip.com/download/linux/latest
tar xf noip-duc_3.3.0.tar.gz
cd /home/$USER/noip-duc_3.3.0/binaries && sudo apt install ./noip-duc_3.3.0_arm64.deb
noip-duc -g all.ddnskey.com --username <DDNS Key Username> --password <DDNS Key Password>
```
## Run as a Daemon/Service
### Create service file
```
vi /etc/systemd/system/noip-duc.service
```
```
[Unit]
Description=No-IP Dynamic Update Client
After=network.target
     
[Service]
ExecStart=/usr/bin/noip-duc -g all.ddnskey.com --username <DDNS Key Username> --password <DDNS Key Password>
Restart=always

[Install]
WantedBy=multi-user.target
```
## Reload system, enable, and start service
```
sudo systemctl daemon-reload
sudo systemctl enable noip-duc
sudo systemctl start noip-duc
```
## Check logs for failure
```
sudo journalctl -u noip-duc.service
```
## Uninstalling
```
sudo rm /usr/local/bin/noip-duc 
```


# Ubuntu Beast Commands

```
wget --content-disposition https://www.noip.com/download/linux/latest
tar xf noip-duc_3.3.0.tar.gz
cd /home/$USER/noip-duc_3.3.0/binaries && sudo apt install ./noip-duc_3.3.0_arm64.deb
noip-duc -g all.ddnskey.com --username <DDNS Key Username> --password <DDNS Key Password>
```
## Enable service for automatic start on reboot

## Copy service file to systemd/system

```
cp /noip-duc_3.3.0/debian/service /etc/systemd/system/noip-duc.service

```
## Add line 6: ExecStart=/usr/bin/noip-duc to:

```
vim /etc/systemd/system/noip-duc.service 

```
## Create default file

```
vim /etc/default/noip-duc

```
## Add the following:

NOIP_USERNAME=username
NOIP_PASSWORD=password
NOIP_HOSTNAMES=example.ddns.net

## Reload and start services

```
sudo systemctl daemon-reload
sudo systemctl enable noip-duc
sudo systemctl start noip-duc

```
## Check status

```
sudo systemctl status noip-duc

```
