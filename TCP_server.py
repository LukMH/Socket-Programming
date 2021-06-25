from socket import*
import datetime # for getting the current year
import hashlib # for using SHA256

def server_function(inputFromClient):
  currentDate = datetime.datetime.now() # get the current date and time
  currentYear = str(currentDate.year) # store the current year in the variable
  concatenation = "COMP5311" + inputFromClient.decode('utf-8') + currentYear # concatenating the strings
  sha256 = hashlib.sha256() # SHA256 is chosen
  sha256.update(bytes(concatenation,'utf-8')) # input the concatenated string to the hash
  return sha256.hexdigest() # return digest (hexadecimal digits)

serverName = 'localhost'
serverPort = 12345 # cannot be a integer greater than 65535
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((serverName, serverPort))
serverSocket.listen(1) # enable the server to accept connections
print('The server is now ready to receive')

while 1: # while true
  connectionSocket, addr = serverSocket.accept()
  inputFromClient = connectionSocket.recv(1024) # receive the data from the socket
  print('From client:',inputFromClient.decode('utf-8'))
  hexDigest = server_function(inputFromClient) # apply the server_function
  print('After applying the server_function:\n'+hexDigest)
  connectionSocket.send(bytes(hexDigest,'utf-8')) # send the hexDigest to the socket
  connectionSocket.close()
