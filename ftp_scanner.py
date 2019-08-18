from ftplib import FTP




with open("ftp_hosts1.txt") as file:
	for line in file:
		line = line.strip() #preprocess line
		try:
			print("Try to connect to: {}".format(line))
			ftp = FTP(line, timeout=3)

		except:
			print("connection to {} failed!".format(line))
		else:
			print("connection to {} successed!".format(line))

