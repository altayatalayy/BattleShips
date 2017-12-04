import threading, queue, socket, pickle

class DataThread(threading.Thread):
	
	def __init__(self,connections):
		threading.Thread.__init__(self)
		self.connections = connections
	
	def run(self):
		self.q = queue.Queue()
		while True:
			for client in self.connections:
				data = client.recv(4096).decode('utf-8')
				if not data:
					break
				self.q.put(data)

	def give_queue(self): 
		return self.q

class ServerHandler(threading.Thread):
	
	def __init__(self,Q,Ship,Board,func):
		threading.Thread.__init__(self)
		self.Q = Q
		self.Ship = Ship
		self.Board = Board
		self.func = func
	
	def run(self):
		while True:
			self.func(self.Q,self.Ship,self.Board)


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