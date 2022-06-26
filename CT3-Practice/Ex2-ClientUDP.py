from http import client
import socket 
c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Socket Created in client")

msg = "Hello UDP kid"

c.sendto(msg.encode("utf-8"), ("localhost",8080))

c,addr = c.recvfrom(1024)

print(c.decode("utf-8"))

c.close()

