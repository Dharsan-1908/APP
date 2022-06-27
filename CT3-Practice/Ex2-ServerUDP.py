import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("localhost",8080))

while True:
    print("Waiting for client")
    c,addr = s.recvfrom(1024)
    print("Recieved message: ",c,"From",addr)