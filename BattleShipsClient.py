import socket

host = "127.0.0.1"
port = 0

server  = ("127.0.0.1",5000)
s.bind((host,port))
s.setblocking(0)

alias = Name

guess = input("Cordinates --> ").strip()

while guess != "Quit"
  if guess != " ":
  	s.sendto(alias+guess, server)
  guess = input("Cordinates --> ").strip()
