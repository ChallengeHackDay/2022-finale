#!/bin/sh
service ssh start
/root/knock/knockd -c /root/knock/knockd.conf -D -v &
httpd-foreground