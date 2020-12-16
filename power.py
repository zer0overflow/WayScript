import os, socket

def log(data):
	f = open('log.log', 'a')
	f.write(data)
	f.close()

while 1:
	sock = socket.socket()
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	sock.bind(('0.0.0.0', 8080))
	sock.listen(1)
	print("Waiting for connection!")
	c, addr = sock.accept()
	log("Connected to %s through port %d" % addr)
	while c:
		c.settimeout(2)
		command = c.recv(1024).decode()
		log("COMMAND: %s" % command)
		if command == "shutdown":
			print("SHUTTING DOWN")
			os.system('systemctl suspend')
		elif command == "check":
			print("CHECKED")
		else:
			print("print no data recieved")
		break
	sock.close()

