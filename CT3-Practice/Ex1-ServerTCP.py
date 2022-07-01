import socket

s = socket.socket()
print("Socket Created")

s.bind(("localhost",8080))

s.listen(3)
print("Waiting for connections")

while True:
    c,addr = s.accept()
    name = c.recv(1024)
    
    print("Connected with" , addr, name.decode("utf-8"))
    c.send(b"Welcome to the server ")
    
    c.close()