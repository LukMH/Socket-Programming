from socket import*

serverName = 'localhost'
serverPort = 12345 # cannot be a integer greater than 65535
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

myInput = input('Input something: ') # get user's input
clientSocket.send(bytes(myInput,'utf-8')) # send the input to the socket
result = clientSocket.recv(1024) # receive the data from the socket
print('(From server)\nThe digest of SHA256 of the input (hexadecimal digits):\n'+result.decode('utf-8'))
clientSocket.close()
