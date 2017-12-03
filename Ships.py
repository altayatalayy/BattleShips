from random import randint


class warShip():
	#number_of_ships = 0
	def __init__(self,board_size,player= 1):
		self.size = board_size
		self.ranking = player
		#number_of_ships += 1

	def getCordinates(self):
		cord_x = randint(1,self.size)
		cord_y = randint(0,self.size-1)
		if self.ranking == 1:
			cord_x = (cord_x-1)*3
		else:
			cord_x = cord_x*3-1
		self.cord_x = cord_x
		self.cord_y = cord_y
		return cord_x, cord_y

	def getShot(self,guess_x,guess_y):
		if self.cord_x == guess_x and self.cord_y == guess_y:
			return True
		return False


class admiralShip(warShip):
	pass
		