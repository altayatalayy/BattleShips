from random import randint
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("Boardsize",help="Board size",choices=["small","normal","big"])

board_size = parser.parse_args().Boardsize

if board_size == "small":
  Bsize, turns, length_of_admiralShip, number_of_ships= 4, 3, 1, 1
elif board_size == "normal":
  Bsize, turns, length_of_admiralShip, number_of_ships = 6, 4, 2, 2
elif board_size == "big":
  Bsize, turns, length_of_admiralShip, number_of_ships = 8, 5, 3, 3


class warShip():

  number_of_warShips = 0
 
  def __init__(self):
    
    warShip.number_of_ships += 1
  
  @staticmethod  
  def getPosition(Bsize):
    position_x = randint(0, Bsize - 1)
    position_y = randint(0, Bsize - 1)
    return position_x,position_y
  
  @staticmethod
  def getShot(position_x,position_y,guess_x,guess_y):
    if position_x = guess_x and position_y == guess_y
      return True 
    return False
  
  



class admiralShip(warShip):
 
  rotation_of_ship = randint(0,1) # if 1 rotation is vertical
  
  def __init__(self):
    super.__init__()

    
  def position_of_admiral(self):
    if self.rotation_of_ship == 1:
      if x = 2:
        while position_y+1 >Bsize:
          position_y = randint(0, Bsize - 1)
        position_x,position_y,position_y+1
      elif x=3:
        while position_y+1 >Bsize or position_y-1<0:
          position_y = randint(0, Bsize - 1)
        position_x,position_y-1,position_y,position_y+1

    else:
      if x = 2:
        while position_x+1 >Bsize:
          position_x = randint(0,Bsize-1)
        position_x,position_x+1,position_y
      elif x=3:
        while position_x+1 >Bsize or position_x-1<0:
          position_x = randint(0,Bsize-1)
        position_x-1,position_x,position_x+1,position_y



  

# while warShip.number_of_warShips < number_of_ships:
#   # create 1 normal ship , on a difrent position
#   pass

ship1 = admiralShip()


board1 = [["0"]*Bsize for i in range(Bsize)]
mid_board = ["|"] 
final_board = []
for row in board1:
  final_board.append(row)
  final_board.append(mid_board[0])
  final_board.append(row)

# final_board = [row,mid_board[0],row for row in board1]

def print_board(board):
  i =0
  for row in board:
    if i%3 == 0:
      print(' ')
      print(' '.join(row),end= ' ')
    else:
      print(' '.join(row),end= ' ')
    i +=1

print_board(final_board)


points = 0
for turn in range(turns):
  print("Turn:",turn+1)

  guess_row = int(input("Guess Row: "))
  guess_col = int(input("Guess Col: "))


  if admiralShip.getShot(guess_row,guess_col) == True:
    print("Congratulations! You win!")
    break
  elif warShip.getShot(guess_row,guess_col) == True:
    points +=1
    print("Congratulations! You sunk my Battleship")
    final_board[guess_row][guess_col] = "X"
    print_board(final_board)
  else:
    if turn == turns-1:
      print("Game Over")
    elif (guess_row < 0 or guess_row > Bsize) or  (guess_col < 0 or guess_col > Bsize):
      print("Oops, that's not even in the ocean.")
    elif(board[guess_row][guess_col] == "X"):
      print("You guessed that one already.")
    else:
      print("You missed my battleship!")
      final_board[guess_row][guess_col] = "X"
      print_board(final_board)



