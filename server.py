import socket 
import time
import random
from _thread import start_new_thread

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 


IP_address = "127.0.0.1"
Port = 5000

server.bind((IP_address, Port)) 

server.listen(100) 
list_of_clients = [] 
def clientthread(): 
	while True: 
			message_to_send =str(random.randrange(1,10000)) 
			i=0
			for clients in list_of_clients: 
				if clients[1] == key: 
					try:
						clients[0].send(bytes(message_to_send, 'utf-8')) 
						i+=1
					except:
						del list_of_clients[i]
						conn.close()
			time.sleep(5)

start_new_thread(clientthread, ())
while True: 
	conn, addr = server.accept()
	name = (conn.recv(1024)).decode('utf-8')
	key = (conn.recv(1024)).decode('utf-8')
	list_of_clients.append([conn, key, name])
	print("{}:{} connected".format(addr[0],addr[1]))
conn.close() 
server.close() 
