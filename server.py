import subprocess as sp
import socket
import os

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ip = "192.168.43.227"
port = 1234
s.bind((ip,port))
s.listen()
c_ses, c_add = s.accept()

while True:
	data = c_ses.recv(1000)
	cmmnd = data.decode()
	
	if "install" in cmmnd and "Hadoop" in cmmnd:
		os.system("ansible-playbook /root/Desktop/reps/conf_hadoop.yml")
		output = "hadoop installed"
	
	elif "stop" in cmmnd and "firewall" in cmmnd:
		os.system("firewalloff")
		output = "firewall flushed"
	
	elif "install" in cmmnd and "docker" in cmmnd:
		os.system("ansible-playbook /root/Desktop/reps/ansible_docker.yml")
		output = "docker installed"

	elif "setup" in cmmnd and "server" in cmmnd:
		os.system("ansible-playbook /root/Desktop/reps/httpd.yml")
		output = "server has been setup"

	elif "click" in cmmnd:
		os.system(cmmnd)
		output = "http://192.168.43.227:/pic.png"
	else:
		output = sp.getoutput(cmmnd)

	output = output.encode()
	c_ses.send(output)
