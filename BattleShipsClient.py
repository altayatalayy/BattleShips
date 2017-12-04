import socket, pickle, time, getopt, sys, queue
from Threads import ClienThread

def usage():
  print(''' 
    -j or --host                    set host

    -p or --port                    set port number

    -h or --help                    to learn the usage
 ''')

host = "127.0.0.1"
port = 8000

try:
  opts,args = getopt.getopt(sys.argv[1:],"hj:p:",["help","host,""port"])
except getopt.GetoptError as err:
  print(str(err))
  usage()
  sys.exit()

for o,a in opts:
  if o in ("-h","--help"):
    usage()
    sys.exit()
  elif o in ("-j","--host"):
    host = int(a)
  elif o in ("-p","--port"):
    port = int(a)



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


try:
	clientsocket = socket.socket()
	clientsocket.connect((host,port))
except Exception as e:
	print(str(e))
	clientsocket.close()
	time.sleep(1)
	quit()

def getGuess():
  guess = input("Cordinates --> ").encode("utf-8") # with a comma in between.
  return guess



alias = input("Enter user name: ").encode("utf-8")
guess = getGuess()

q = queue.Queue()
clienThread = ClienThread(q,clientsocket,print_board())
clienThread.start()

while True:
  if guess:
    clientsocket.send(alias+guess)
  else:
    clientsocket.send("".encode("utf-8"))  
    break

  guess = getGuess()

     



print("\n\nClosing client socket.\n")
clientsocket.close()
time.sleep(1)
sys.exit()


