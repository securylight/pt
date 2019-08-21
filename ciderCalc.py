import ipaddress

net = ipaddress.ip_network("xxx.xxxx.xxx.xxx/yy")
for a in net:
	print(a)
