import socket 
import select 
import sys 

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
IP_address = "127.0.0.1"
Port = 5000 
server.connect((IP_address, Port)) 
server.send(bytes(input("Enter you name:"), 'utf-8'))
server.send(bytes(input("Enter server ID OR Creat server ID:"), 'utf-8'))

while True: 
	message = server.recv(1024) 
	print(message.decode('utf-8')) 	

	
server.close() 
