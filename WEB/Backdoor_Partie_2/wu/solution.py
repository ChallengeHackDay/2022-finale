import socket
import base64

SERVER_IP = "127.0.0.1"
SERVER_PORT = 34865
BUFFER_SIZE = 65507

for i in range(4):
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((SERVER_IP,22))
    data = "tok"
    clientSocket.send(data.encode())

    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((SERVER_IP,80))
    data = "tok"
    clientSocket.send(data.encode())

print("Opened")
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