
## Unable to set NAT network adapter name 

* https://www.youtube.com/watch?v=Hndr4EG_zOQ


## If UUID Error

A universally unique identifier (UUID) is a string of characters used to identify a specific virtual disk. 
The UUID of a virtual disk can be changed for various reasons, such as to avoid duplication or to keep the virtual disk separate from others with the same name

## Commands Windows

* c:\> cd "C:\Program Files\Oracle\VirtualBox\"
* c:\> VBoxManage.exe internalcommands sethduuid "D:\NewVM\myDisk1.vdi"

## Commands Linux

* VBoxManage internalcommands sethduuid "/var/vdisks/myDisk1.vdi"
