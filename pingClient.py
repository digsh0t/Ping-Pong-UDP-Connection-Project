from socket import *
import time
serverIP = '192.168.35.1'
serverPort = 12000
recv = 0
loss = 0
for i in range (10) :
	clientSocket = socket(AF_INET, SOCK_DGRAM)
	sendtime = time.time()
	clientSocket.sendto('ping'.encode(), (serverIP, serverPort))
	while time.time() - sendtime < 1 :
		recvMes,serverAddr = clientSocket.recvfrom(1024)
		if recvMes == 'pong' :
			recvtime = time.time() - sendtime
			formattedTime = round(recvtime*1000, 3)
			print('Received pong after ' + str(formattedTime) + 'ms')
			clientSocket.close()
			recv += 1
			break;

	if recvMes != 'pong' :
		print("Can't connect to server")
		loss += 1
		clientSocket.close()

print('10 packets transmitted, ' + str(recv) + ' received, ' + str(loss) + ' packet loss') 
