import socket

c = socket.socket()

c.connect(("localhost",8088))

name = input("Enter your name: ")

c.send(name.encode())

recvData = c.recv(1024)
print(str(recvData.decode('utf-8')))

c.close()