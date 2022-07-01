import socket

c = socket.socket()

c.connect(("localhost",8080))

name = input("Enter your name: ")

c.send(bytes(name.encode()))

recvData = c.recv(1024)

print(recvData.decode("utf-8"), name)