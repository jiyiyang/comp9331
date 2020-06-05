class Server():
	def _init_(self,block_duration):
		self.block = {}
		self.offline = {}
		self.block_duration = block_duration
		with open('credentials.txt') as f:
	     	content = f.readlines()
	    self.user = {}
		for i in content:
			user[i.split()[0]] = {}
			user[i.split()[0]]["pw"] = i.split()[1].replace('\n','')
			user[i.split()[0]]["status"] = 2
		    # status: online=1, offline=2, blocked=3
			user[i.split()[0]]["active_time"] = ''
		    # 活跃时间暂时给空字符
			user[i.split()[0]]["fail count"] = 0
		    # 登陆失败次数
			user[i.split()[0]]["ban timestamp"] = ''
		    # 登陆三次失败的时间戳
		    user[i.split()[0]]["address"] = ('','')

		self.address = ('localhost',port_number)
		self.port = ...
		self.Socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.Socket.bind(self.address)
		self.Socket.listen()
		timeout = threading.Thread(target=self.timeout(), args=(,))
		timeout.start()
		while True:
			conn,addr = self.Socket.accept()
			t = threading.Thread(target = tcp,args = (conn,addr))
			t.start()
			
				
		
	def tcp(self,conn,addr):
		login = pickle.loads(conn.recv(1024))
		# login = (self.user_name,self.pw)
		user_name = login[0]
		pw = login[1]
		status, a = self.auth(user_name,pw)
		if status == True:
			self.precense_broadcast(user_name)
			conn.send('connection established')
			print('connected to xxx')
			while True:
				command = conn.recv()
				if command == "whoelse": #if reply from server confirms that connection is established
					result = self.precense_broadcast()
					conn.send(pickle.dumps(result))
				elif command == xxx:
					self.xxx()
				elif...
		else:
			# 打包登陆失败信息，返回给客户端，告诉对方为什么失败
			conn.send(pickle.loads(a))
			# 关闭tcp 连接
			conn.close()

	def timeout(self):
		while 1:
			time.sleep(1)
			for i in self.user.keys():
				if user[i]['status']==1:
					if type(user[i]['active_time']) == float:
						if time.time() - user[i]['active_time'] > timeout_time:
							user[i]['status'] = 2

	def auth(self):
		...

	# 收到客户端的登出请求时，改变登录状态为2，登出
	def logout(self,user_name):
		self.user[user_name]['status'] = 2

	def broadcast(self,msg,user_name):
		for i in self.user:
			if self.user[i]['status']==1:
				add = self.user[i]['add']
				self.Socket.sendto(msg,add)

	def blocklist(self,user_name,blocked_user):
		# 省略判断字典是否已又某用户的代码
		if user_name not in self.block:
			self.block[user_name] = set()
		self.block[user_name].add(blocked_user)
		
	def unblock(self,user_name,blocked_user):
		# 省略判断字典是否已又某用户的代码
		self.block[user_name].remove(blocked_user)

	def check_offline_msg(self):
		if user_name in self.offline:
			for sender in self.offline[user_name]:
				for j in self.offline[user_name][sender]: #self.offline[user_name][sender] should be the list of offline message from this sender
					if j['read_or_not'] == False:
						self.conn.send((sender, j['msg'], j['time']))
						j['read_or_not'] = True


	def forward(self,sender,receiver,message):
		if receiver in self.user.keys():
			if self.user[receiver]['status']==1:
				add = self.user[receiver]['add']
				if sender not in self.block[receiver]:
					self.Socket.sendto(message,add)
				else:
					# tell sender that you have been blocked by receiver
			else:
				# offline msg
				if receiver not in self.offline:
					self.offline[receiver]={}
					self.offline[receiver][sender]=[{'msg':message,'time':time.time(),'read_or_not':False}]
				self.offline[receiver][sender].append({'msg':message,'time':time.time(),'read_or_not':False})
		else:
			self.conn.send("user doesn't exist")

	def list_online(self):
		result = []
		for i in self.user.keys():
			if self.user[i]['status'] == 1:
				result.append(i)
		return result

	def online_hist(self,since):
		result = []
		for i in self.user.keys():
			if time.time() - self.user[i]['active_time']<since:
				result.append(i)
		return result

	def precense_broadcast(self,user_name):
		for i in self.user.keys():
			if self.user[i]['status']==1:
				self.Socket.sendto(f'{user_name} is online',self.user[i]['add'])

	# def listen(self):
	# 	while True:
	# 		msg = self.conn.recv(...)
	# 		if msg == ..:
	# 			if auth(..):
	# 				self.broadcast:
	# 			else:
	# 				self.conn.send("not logged in...etc etc")
	# 		if msg == ..:
	# 			if auth(..):
	# 				self.broadcast:
	# 			else:
	# 				self.conn.send("not logged in...etc etc")

def main():

	server = Server(sys.argv[1])
