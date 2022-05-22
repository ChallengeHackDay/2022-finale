import base64
import socket

SERVER_IP = 'SERVER IP'
SERVER_PORT = SERVER PORT
BUFFER_SIZE = 65507 #max size of udp

command = bytearray(input("Commande : ").encode('utf8'))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server = (SERVER_IP, SERVER_PORT)

sock.sendto(base64.b64encode(b"hackday"),server)
data, addr = sock.recvfrom(BUFFER_SIZE)
result = base64.b64decode(data).decode('utf8')
print(result, end="\n\n")

sock.sendto(base64.b64encode(command), server)
data, addr = sock.recvfrom(BUFFER_SIZE)
result = base64.b64decode(data).decode('utf8')
print(result)
