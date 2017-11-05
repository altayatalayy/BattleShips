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
port = 5000



try:
	clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#clientsocket.setblocking(0)
	#clientsocket.setdefaulttimeout(50)
	clientsocket.connect((host,port))
except socket.error:
	print("Error while creating client-socket")
	socket.shutdown()
	socket.close()
	time.sleep(2)
	quit()



alias = input("Enter user name: ").strip().lower().capitilaze()
clientsocket.send(alias)

guess = input("Cordinates --> ").strip() # with a comma in between.

quitting = False
while not quitting:
  if guess != " " and type(guess)==int:
  	clientsocket.send(guess)
  elif guess == "Quit":
    print("\nQuiting from server")
    socket.shutdown()
    socket.close()
    time.sleep(2)
    quit()

  else:
  	print("Invalid input")
    guess = input("Cordinates --> ").strip()
  try:
  	data = clientsocket.recv(1024)
  	data.decode('utf-8')
  	if data[:5] == "Board":
  		print_board(data[5:])
  	else:
  		print(str(data))
  except Exception:
    print("\nSome really big problem")

  guess = input("Cordinates --> ").strip()


socket.shutdown()
print("\nEmergency shut down.")
socket.close()
time.sleep(2)
quit()


