import socket

host  = "127.0.0.1"
port  = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host,port))

print("Server Started")

quitting = False

while not quitting:
	data, addr = s,revfrom(1024)
	data = data.decode("utf-8")
	print("Data from: "+str(addr),end = "  ")
	print("From connected user: "+data)
	data1,data2 = data.split(" ")



	s.sendto(new_status.encode("utf-8"),addr)
	
