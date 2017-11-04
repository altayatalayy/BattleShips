import socket
import time

def print_board(board):
	# to print board with data that has came from server, Server will send the current status of board at each turn. 
  i =0
  for row in board:
    if i%3 == 0:
      print(' ')
      print(' '.join(row),end= ' ')
    else:
      print(' '.join(row),end= ' ')
    i +=1


host = "127.0.0.1"
port = 0



try:
	clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	clientsocket.setblocking(0)
	clientsocket.setdefaulttimeout(50)
	clientsocket.connect((host,port))
except socket.error:
	print("Error while creating client-socket")
	socket.shutdown()
	socket.close()
	time.sleep(2)
	quit()



alias = input("Enter your name: ").strip().lower().capitilaze()
clientsocket.send(alias)

guess = input("Cordinates --> ").strip()

quitting = False
while not quitting
  if guess != " " and type(guess)==int:
  	clientsocket.send(guess)
  else:
  	print("Invalid input")
  try:
  	data = clientsocket.recv(1024)
  	data.decode('utf-8')
  	if type(data) == list:
  		print_board(data)
  	else:
  		print(str(data)

  guess = input("Cordinates --> ").strip()


