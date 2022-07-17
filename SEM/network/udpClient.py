import socket

c = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

msg = b'Hello this is Meow Cat with out teeth'
c.sendto(msg,("localhost",8080))

c.close()