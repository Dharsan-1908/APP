import socket

c = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

msg = b"Hello world!"
c.sendto(msg,('localhost',8080))

s,addr = c.recvfrom(1024)

print("Server says",s)

c.close()