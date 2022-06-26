import socket 
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Socket Created in server")

s.bind(("localhost",8080))

while True:
    c, addr = s.recvfrom(1024)
    print("Connected with", addr, c.decode("utf-8"))
    name = bytes("hello iam noob")

    c.sendto(name.encode(), addr)