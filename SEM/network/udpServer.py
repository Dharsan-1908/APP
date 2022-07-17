import socket 

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(("localhost",8080))

while True:
    c, addr = s.recvfrom(1024)
    print(c.decode('utf-8'))