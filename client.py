# client app

import sys
import socket
import threading
import pickle
class Client():
	def __init__(self,...):
		self.server_address = ('localhost',port_number)
		self.port = ...
		self.Socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.Socket.connect(self.server_address)
		self.login = False
		while True:
			self.user_name = input('user_name')
			self.pw = input('password')
			login = pickle.dumps((self.user_name,self.pw))
			self.Socket.send(login)
			reply = self.Socket.recv(....)
			if reply == "connection established": #if reply from server confirms that connection is established
				command = threading.Thread(target=self.command_line(), args=(,))
				listen = threading.Thread(target=self.listen(), args=(,))
				xxx = threading.Thread(target = other)

				threadings = [command,listen,xxx,...]
				for i in threadings:
					i.start()
					
			else:
				print(reply)
				print('try again..')#login failed, based on server reply message


	def command_line(self):
		while self.lgin:
			command = input()
			commands = command.split()
			if commands[0] == ...:
				self.send_msg()
			elif commands[0] == "whoelse":
				self.list_online()
			elif commands[0] == ...:
				self.online_history():
			elif commands[0] = ...:
				self.blacklist()

	def listen(self):
		# 用户监听服务器发来的广播信息，上下线信息等等
		while self.login:
			self.ConnSock.listen()
			msg = self.ConnSock.recv(1024)....
			print(msg)

	def send_msg(self,receiver,message):
		self.ConnSock.send(pickle.dumps((receiver,message)))

	def list_online(self):
		self.ConnSock.send("whoelse")
		result = pickle.loads(self.ConnSock.recv(1024))
		# result = [all online users]
		for i in result:
			print(i)
	
	def online_history(self):
		...
	
	def blacklist(self):
		...

	def logout(self):
		self.login = False
	