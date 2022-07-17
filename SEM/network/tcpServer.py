# import socket

# s = socket.socket()
# print("Socket created successfully")

# s.bind(("localhost",8088))
# s.listen(5)

# while True:
#     c ,addr = s.accept()
#     print("Connection successful noob ",addr)
#     recvMessage = c.recv(1024)
#     print(recvMessage.decode())
#     strSend = recvMessage.upper()
#     c.send(strSend)
#     c.close()

import socket 

server = socket.socket()
server.bind(("localhost",8080))
server.listen(5)

while True:
    client, addr  = server.accept()
    recvMess = client.recv(1024)
    dataUpper = recvMess.decode().upper()
    client.send(dataUpper.encode())
    client.close()