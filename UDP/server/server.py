from socket import *

serverPort = 8888
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("The server is ready to receive: ")
while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    x = str(message, encoding="utf-8")  # convert bytes to string
    print(x)
    n = int(x)  # convert string to integer
    # product1 = 1 # compute the factorial of n
    # for i in range(n):
    #    product1 = product1 * (i+1)
    # modifiedMessage = str(product1) # convert integer to string
    sum1 = 0
    for i in range(n):
        sum1 = sum1 + (i + 1)
    modifiedMessage = str(sum1)  # message.upper()
    serverSocket.sendto(bytes(modifiedMessage, encoding="utf-8"), clientAddress)
