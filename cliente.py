import socket
import threading
import sys
import pickle

class Cliente():
	def __init__(self, host="localhost", port=4000):

		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.connect((str(host), int(port)))

		msg_rec = threading.Thread(target = self.msg_rec)
		msg_rec.daemon = True
		msg_rec.start()

		while True:
			msg = input('>')
			if msg != 'salir':
				self.msg_send(msg)
			else:
				self.sock.close()
				sys.exit()

	def msg_rec(self):
		while True:
			try:
				data = self.sock.recv(1024)
				if data:
					print(pickle.loads(data))
			except:
		 		pass 

	def msg_send(self, msg):
		self.sock.send(pickle.dumps(msg))

c = Cliente()