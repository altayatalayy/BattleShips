import socket
import time
import pickle


def print_board(board):
	# to print board with data that has came from server, Server will send the current status of board at each turn. 
  i =0
  for row in board:
    if i%3 == 0:
      print(' ')
      print('\t\t\t',end = '')
      print(' '.join(row),end= ' ')
    else:
      print(' '.join(row),end= ' ')
    i +=1


host = "127.0.0.1"
port = 9000



try:
	clientsocket = socket.socket()
	clientsocket.connect((host,port))
except Exception as e:
	print(str(e))
	socket.close()
	time.sleep(2)
	quit()



alias = input("Enter user name: ").encode("utf-8")
guess = input("Cordinates --> ").encode("utf-8") # with a comma in between.




while True:
  if guess:
    clientsocket.send(alias+guess)
  else:
    clientsocket.send("Quit".encode("utf-8"))  
    break
  data = pickle.loads(clientsocket.recv(4096),encoding="utf-8")
  print_board(data)
  guess = input("\nCordinates --> ").encode("utf-8")

     



print("\n\nClosing client socket.\n")
clientsocket.close()
time.sleep(2)
quit()


