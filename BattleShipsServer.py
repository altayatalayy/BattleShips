import socket
from random import randint
import argparse
import sys
import threading
import time


parser = argparse.ArgumentParser()
parser.add_argument("Boardsize",help="Board size",choices = ["small","normal","big"])
board_size = parser.parse_args().Boardsize

if board_size == "small":
  Bsize = 6
elif board_size == "normal":
  Bsize = 8
elif board_size == "big":
  Bsize = 10

board1 = [["0"]*Bsize for i in range(Bsize)]
mid_board = ["|"] 
final_board = []
for row in board1:
  final_board.append(row)
  final_board.append(mid_board[0])
  final_board.append(row)





# ------- Server-------

port  = 5000

try:
  serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  serversocket.bind((socket.gethostname(),port))
  serversocket.listen(3)
except socket.eror:
	print("Problem while starting the server")
  time.sleep(2)
  quit()

print("Server Started")



connections = {}
quitting = False
i = 0
while not quitting:
  try:
    clientsocket,addr = serversocket.accept()
  except socket.timeout:
    print("Time out eror")
  except Exception :
    print("Eror while connecting to the client")
 
	alias = serversocket.recv(1024) 
	alias = alias.decode("utf-8")
	if addr not in connections:
    if i ==0:
      user1 = addr
    elif i == 1:
      user2 = addr
    connections[addr] = alias
    i += 1 
  elif alias == "Quit":
    quitting = True

  print("Data from: "+str(addr)+" -->"+str(data))
	if type(data) == int and len(data)>1:
    data1,data2 = data.split(" ")
  else:
    new_data = "You must enter 2 numbers"
    serversocket.send(new_data)

  




	serversocket.send(new_status)
	
