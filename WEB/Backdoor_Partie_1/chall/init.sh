#!/bin/sh
/usr/bin/python3 /home/user/backdoor.py &
service vsftpd start
httpd-foreground