import socket
from random import randint
import argparse
import time


parser = argparse.ArgumentParser()
parser.add_argument("Boardsize",help="Board size",choices = ["small","normal","big"])
board_size = parser.parse_args().Boardsize

if board_size == "small":
  Bsize = 6
  number_of_turns = 4
elif board_size == "normal":
  Bsize = 8
  number_of_turns = 5
elif board_size == "big":
  Bsize = 10
  number_of_turns = 6

board1 = [["0"]*Bsize for i in range(Bsize)]
mid_board = ["|"] 
final_board = []
for row in board1:
  final_board.append(row)
  final_board.append(mid_board[0])
  final_board.append(row)


class warShip():

  number_of_warShips = 0
 
  def __init__(self):
    
    warShip.number_of_ships += 1
  
  @staticmethod  
  def getPosition(Bsize): # Needs serious maintenance
    position_x = randint(0, Bsize - 1)
    position_y = randint(0, Bsize - 1)
    return position_x,position_y
  
 def getShot(position_x,position_y,guess_x,guess_y):
    if position_x = guess_x and position_y == guess_y
      return True 
    return False
  
  

class admiralShip(warShip):

  def __init__(self):
    super.__init__(self)



# -----------------Server-----------------

port  = 5000

try:
  serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  serversocket.bind((socket.gethostname(),port))
  serversocket.listen(2)
except socket.eror:
	print("Problem while starting the server")
  time.sleep(2)
  quit()

print("Server Started")

try:
  clientsocket,addr = serversocket.accept()
except socket.timeout:
  print("Time out eror")
except Exception :
  print("Eror while connecting to the client")

quitting = False


if addr not in connections:
  if i ==0:
    clientsocket1 = clientsocket # not sure if this has any meaning at all
  elif i == 1:
    clientsocket2 = clientsocket
  connections[addr] = alias
  i += 1 
elif alias == "Quit":
    quitting = True

connections = {}
i = 0


while not quitting:

  #Player1
  data1 = clientsocket1.recv(1024) 
	data1 = data1.decode("utf-8")
	print("Data from: "+str(addr)+" -->"+repr(data))
	if type(data1) == int and len(data1)>1:
    data1_1,data1_2 = data1.split(",")
  else:
    data = "You must enter 2 numbers"
    clientsocket1.send(data)
  if data1_1:
    data1_1 /=3
    if admiralShip2.getShot(data1_1,data1_2) == True:
      print("Player1 sunk Player2's admiral ship")
      data = "Congratulations! You win!"
      clientsocket1.send(data)
      print("Quitting from server")
      break
    elif warShip2.getShot(data1_1,data1_2) == True:
      points1 +=1 
      print("Player1 sunk Player2's Battleship")
      final_board[data1_1][data1_2] = "X"
      data = "Player1 sunk Player2's Battleship"
      clientsocket.send(data)
      
    else:
      if (data1_1 < 0 or data1_1 > Bsize) or  (data1_2 < 0 or data1_2 > Bsize):
        print("Player1 --> out of range.")
        data = "Out of range"
        clientsocket1.send(data)
      elif(final_board[data2_1][data2_2] == "X"):
        print("Player1 --> already guessed.")
        data = "Already guessed that one"
        clientsocket1.send(data)
      else:
        print("Player1 --> missed")
        final_board[guess_row][guess_col] = "X"

  #Player2
  data2 = clientsocket2.recv(1024)
  data2 = data2.decode("utf-8")
  print("Data from: "+str(addr)+" -->"+repr(data))
  if type(data2) == int and len(data2)>1:
    data2_1,data2_2 = data2.split(",")
  else:
    data = "You must enter 2 numbers"
    clientsocket2.send(data)
  if data2:
    data2_1 = (data2_1-2)/3
    if admiralShip1.getShot(data2_1,data2_2) == True:
      print("Player2 sunk Player1's admiral ship")
      data = "Congratulations! You win!"
      clientsocket2.send(data)
      print("\nQuitting from server")
      break
    elif warShip1.getShot(data2_1,data2_2) == True:
      print("Player2 sunk Player1's Battleship")
      points2 += 1
      final_board[data2_1][data2_2] = "X"
      data = "Player2 sunk Player1's Battleship"
      clientsocket.send(data)
      
    else:
      if (data2_1 < 0 or data2_1 > Bsize) or  (data2_2 < 0 or data2_2 > Bsize):
        print("Player2 --> out of range.")
        data = "Out of range"
        clientsocket2.send(data)
      elif(final_board[data2_1][data2_2] == "X"):
        print("Player2 --> already guessed.")
        data = "Already guessed that one"
        clientsocket2.send(data)
      else:
        print("Player2 --> missed")
        final_board[guess_row][guess_col] = "X"
  
  clientsocket.send("Board"+final_board)      









  
clientsocket1.close()
clientsocket2.close()
clientsocket.close()
time.sleep(2)
quit()	
