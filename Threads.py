import threading, queue, socket, pickle

#-----------------Server Side-----------------
class DataThread(threading.Thread):
	
	def __init__(self,connections):
		threading.Thread.__init__(self)
		self.connections = connections
		self.Q = queue.Queue()
	
	def run(self):
		while True:
			for client in self.connections:
				data = client.recv(4096).decode('utf-8')
				if not data:
					break
				self.Q.put(data)

	def give_queue(self): 
		return self.Q


class ServerHandler(threading.Thread):
	
	def __init__(self,Q,Ship1,Ship2,Board,func):
		threading.Thread.__init__(self)
		self.Q = Q
		self.Ship1 = Ship1
		self.Ship2 = Ship2
		self.Board = Board
		self.func = func
	
	def run(self):
		while True:
			self.func(self.Q,self.Ship1,self.Ship2,self.Board)




#-----------------Client Side-----------------
class ClienThread(threading.Thread):
	
	def __init__(self,Q,client_socket):
		threading.Thread.__init__(self)
		self.Q = Q
		self.client_socket = client_socket
	
	def run(self):
		while True:
			data = pickle.loads(self.client_socket.recv(4096),encoding="utf-8")
			self.Q.put(data)


class ClientPrint(threading.Thread):

	def __init__(self,Q,func):
		threading.Thread.__init__(self)
		self.Q = Q
		self.func = func

	def run(self):
		while True:
			data = self.Q.get()
			self.func(data)





