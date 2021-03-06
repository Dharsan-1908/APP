import socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(("127.0.0.1", 9090))
serverSocket.listen()
while(True):
    (clientConnected, clientAddress) = serverSocket.accept()
    print("Accepted a connection request from %s:%s" %
        (clientAddress[0], clientAddress[1]))
    dataFromClient = clientConnected.recv(1024)
    print(dataFromClient.decode())
    dataFromClient = dataFromClient.decode()
    if(dataFromClient == "ping" or dataFromClient == "PING" or dataFromClient == "Ping"):
        clientConnected.send("pong".encode())
    else:
        clientConnected.send("messageDropped".encode())
