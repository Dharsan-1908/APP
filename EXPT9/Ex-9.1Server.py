import socket            

s = socket.socket()        
print ("Socket successfully created")
host = socket.gethostname()
port = 12345               

s.bind((host, port))        
print ("socket binded to %s" %(port))

s.listen(5)    
print ("socket is listening")           

while True:
    c, addr = s.accept()    
    print ('Got connection from', addr )
    c.send('Thank you for connecting'.encode())
    c.close()
    break