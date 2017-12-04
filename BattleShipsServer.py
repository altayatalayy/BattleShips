import sys, getopt, pickle, threading, time, socket, queue, termcolor
from Ships import warShip # contains ship classes
from Threads import DataThread, ServerHandler


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
  opts, args = getopt.getopt(sys.argv[1:], "hs:t:n:p:j:", ["help","size","turn","number","port","host"])
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

def clientHandler(q,ship,Board):
    data = q.get()
    if data:
        cord_x,cord_y = data[7:].split(',')
    else:
        closeServer()

    if data[:7] == 'Player1':
      data1 = int(cord_x)*3-1
      data2 = int(cord_y) - 1
    elif data[:7] == 'Player2':
      data1 = (int(cord_x)-1)*3
      data2 = int(cord_y) - 1
    
    print(data[:7]+' --> '+str(data1)+','+str(data2))
    
    if data1 < 0 or data2 < 0 or data1 > Bsize*3 or data2 > Bsize-1:
      print(data[:7]+" --> missed the board")
    elif Board[data1][data2] == "X":
      print(data[:7]+" --> guessed already")
    elif ship.getShot(data1,data2):
      print(data[:7]+" --> shot the ship")
      Board[data1][data2] = termcolor.colored('X','green')
    else:
      print(data[:7]+" --> missed")
      Board[data1][data2] = termcolor.colored('X','red')
    
    encoded_board = pickle.dumps(Board)
    for client in connections:
      client.send(encoded_board)
    print('Data sent\n\n')

# -----------------Server-----------------


def startServer(host, port):
  global  serversocket, connections
  
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
  
  while len(connections) != 2:
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
  print('\n')


def closeServer():
  print("Closing server\n")
  serversocket.close()
  time.sleep(1)
  sys.exit()
    

#-----------------Play Game-----------------

startServer(host,port)

dataThread = DataThread(connections)

dataThread.start()
q = dataThread.give_queue()

a = warShip(Bsize)
print(a.getCordinates(),'\n')
b = warShip(Bsize,player = 2)
print(b.getCordinates(),'\n')

serverThread1 = ServerHandler(q,a,final_board,clientHandler)
serverThread2 = ServerHandler(q,b,final_board,clientHandler)

serverThread1.start()
serverThread2.start()


