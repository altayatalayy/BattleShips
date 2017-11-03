import socket
from random import randint
import argparse
import sys
import threading


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

def print_board(board):
  i =0
  for row in board:
    if i%3 == 0:
      print(' ')
      print(' '.join(row),end= ' ')
    else:
      print(' '.join(row),end= ' ')
    i +=1



# ------- Server-------
host  = "127.0.0.1"
port  = 5000

try:
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  s.bind((host,port))
except Exception:
	print("Problem while starting the server")

print("Server Started")

connections = []
quitting = False

while not quitting:
	data, addr = s,revfrom(1024)
	data = data.decode("utf-8")
	if addr not in connections:
		connections.append(addr)
    
	print("Data from: "+str(addr)+" -->"+str(data))
	
	data1,data2 = data.split(" ")



	s.sendto(new_status.encode("utf-8"),addr)
	
