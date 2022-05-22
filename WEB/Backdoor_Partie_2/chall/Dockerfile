FROM httpd:latest

COPY flag6006572441.txt /root/

RUN apt update -yq
RUN apt install git libpcap-dev autoconf gcc make python3 openssh-server -yq
WORKDIR /root/

RUN git clone https://github.com/jvinet/knock.git
WORKDIR /root/knock
RUN autoreconf -fi
RUN ./configure --prefix=/usr/local
RUN make
RUN make install
COPY knockd.conf .

COPY ./public-html/ /usr/local/apache2/htdocs/

RUN mkdir /var/run/sshd
RUN echo 'root:rnxBGVMfqGxa4rK3bGG5kQr5fw3vRCp' | chpasswd
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

COPY backdoor.py /root/
COPY entry.sh /root/entry.sh
WORKDIR /
ENTRYPOINT ["/bin/sh","/root/entry.sh"]