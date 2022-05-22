FROM httpd:latest

COPY flag.txt /root/flag.txt
RUN echo server > /etc/hostname
RUN apt-get update
RUN apt-get install python3 pip -yq

RUN apt-get install vsftpd -yq
COPY vsftpd.conf /etc/vsftpd.conf
RUN mkdir /srv/files
RUN mkdir /srv/files/ftp
RUN usermod -d /srv/files/ftp ftp 

COPY ./ftp/ /srv/files/ftp/

COPY ./public-html/ /usr/local/apache2/htdocs/

RUN mkdir /home/user
COPY backdoor.py /home/user/

COPY init.sh /home/user/
ENTRYPOINT [ "/bin/sh","/home/user/init.sh" ]