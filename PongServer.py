from socket import *
serverIP = '192.168.35.1'
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind((serverIP, serverPort))
print('Server succesfully started')
while True:
	recvMes,clientAddr = serverSocket.recvfrom(1024)
	if recvMes.decode() == 'ping' :
		serverSocket.sendto('pong'.encode(), clientAddr)
