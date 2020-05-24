from socket import *

serverName = 'localhost'  # IP或者主机名
serverPort = 8888
clientSocket = socket(AF_INET, SOCK_DGRAM)  # AF_INET使用IPv4，SOCK_DGRAM 使用UDP
while 1:
    message = input("求1到n的和: ")
    message = bytes(message, encoding="utf-8")
    clientSocket.sendto(message, (serverName, serverPort))
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    modifiedMessage = str(modifiedMessage, encoding="utf-8")
    print(modifiedMessage)
