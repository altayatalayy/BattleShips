import sys, getopt, pickle, threading, time, socket
from Ships import warShip # contains ship classes



#-----------------Intro-----------------

Bsize = 6
number_of_turns = 4
number_of_ships = 1
host = '127.0.0.1'
port  = 8000


def usage():
  print(''' 
    Battle ships game

    -n or --number                  set number of total ships

    -s or --size                    set board size

    -t or --turn                    set number of turns

    -j or --host                    set host

    -p or --port                    set port number

    -h or --help                    to learn the usage

    ''')
  sys.exit()


try:
  opts, args = getopt.getopt(sys.argv[1:], "hs:t:n:p:j", ["help","size","turn","number","host","port"])
except getopt.GetoptError as err:
  print(str(err))
  usage()
  sys.exit()



for o,a in opts:
  if o in ("-h","--help"):
    usage()
  elif o in ("-s","--size"):
    Bsize = int(a)
  elif o in ("-t","--turn"):
    number_of_turns = int(a)
  elif o in ("-n","--number"):
    number_of_ships = int(a)
  elif o in ("-j","--host"):
    host = a
  elif o in ("-p","--port"):
    port = int(a)
  else:
    assert False,"Unhandled Option"




# -----------------Board-----------------

board1 = [["0"]*Bsize for i in range(Bsize)]
mid_board = ["|"] 
final_board = []
for row in board1:
  final_board.append(row)
  final_board.append(mid_board[0])
  final_board.append(list(row))

print("board size = "+str(Bsize))


# -----------------Thread-----------------

def clientHandler():
  pass


# -----------------Server-----------------


def startServer():
  global host, port, serversocket, connections
  
  try:
    serversocket = socket.socket()
    serversocket.bind((host,port))
    serversocket.listen(2)
  except Exception as e:
    print(str(e))
    serversocket.close()
    time.sleep(2)
    sys.exit()
  print("Server Started\n")

  connections = []
  adrress = []
  
  while len(connections) != 1:
    try:
      conn,addr = serversocket.accept()	  
    except Exception as e:
      print(str(e))	  
    finally: 
      if addr not in connections:
        connections.append(conn)
        adrress.append(addr)

  print('Connections: ')
  for addr in adrress:
	  print('[*] '+str(addr))

  

startServer()
a = warShip(Bsize)
print(a.getCordinates())
while True:
 

  #exec(input("--> "))

  # client_thread = threading.Thread(target = clientHandler,args = (client_socket,))
  # client_thread.start()

  data = connections[0].recv(4096).decode('utf-8')

  if "Quit" == str(data):
    break
  
  elif data[:7] == "Player1":

    data1,data2 = data[7:].split(",")
    data1 = (int(data1)-1)*3  # Enter numbers from 1 to Bsize
    data2 = int(data2) - 1 
    print("Player1 --> "+str(data1)+" "+str(data2))

    print(a.getShot(data1,data2))

    if data1 < 0 or data2 < 0 or data1 > Bsize*3 or data2 > Bsize:
      print("Player1 --> missed the board")
    elif final_board[data1][data2] == "X":
      print("Player1 --> guessed already")
    else:
      print("Player1 --> missed")
      final_board[data1][data2] = 'X'

  
  encoded_final_board = pickle.dumps(final_board)
  for con in connections:
    con.send(encoded_final_board)
  print("data sent \n\n")
  

  	

  
  			


  

print("Closing server\n")
serversocket.close()
time.sleep(1)
quit()	
