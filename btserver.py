#!/usr/bin/env python
#coding: utf8 

#imports
from bluetooth import *
import subprocess
import time
import os
from imgdisp import imgdisp


def server():
	#definiere variable server_sock
	server_sock=BluetoothSocket( RFCOMM )
	#binde den socket auf irgendeinen Port, Port 1
	server_sock.bind(("",PORT_ANY))
	#warte auf Anfragen
	server_sock.listen(1)

	port = server_sock.getsockname()[1]
	
	#frei erfundene UUID
	uuid = "94f39d29-7d6d-437d-973b-fba39e49d4aa"

	#publiziere den Service mit UUID
	advertise_service( server_sock, "LEDTABLE",
					   service_id = uuid,
					   service_classes = [ uuid, SERIAL_PORT_CLASS ],
					   profiles = [ SERIAL_PORT_PROFILE ], 
	#                   protocols = [ OBEX_UUID ] 
						)
					   
	print("Waiting for connection on RFCOMM channel %d" % port)

	#Akzeptiere Verbindung mit Client
	client_sock, client_info = server_sock.accept()
	print("Accepted connection from ", client_info)
	
	#smiley face
	imgdisp("/home/pi/led/progs10/smiley-happy.png")
	time.sleep(1)
	imgdisp("/home/pi/led/progs10/black.png")
		

#try damit falls die Verbindung einbricht die exception aufgerufen wird. Siehe unten
	try:
		while True:
			#setze empfangene Strings auf data
			data = client_sock.recv(1024)
			#Falls nichts gesendet wurde, bzw. nur enter gedrückt wurde,
			#bricht die schleife ab
			if len(data) == 0: 
				break
			#gebe empfangenen String aus
			print("received [%s]" % data)
			
			#Command receiving
			if data[0:5] == "TIME ":
				try:
					print(data[5:30])
					os.system("sudo date -s '%s'" % data[5:30])
					#subprocess.Popen(["sudo", "date -s", data[6:29])
				except:
					pass

				
			if data == "hsv":
				try:
					#teste ob ein Prozess bereits am laufen ist
					#Wenn ja, wird None zurückgegeben
					if p.poll() == None:
						print "Can only start one process at a time"
				except:	
					try:
						#starte den subprocess und speichere ihn unter p
						p = subprocess.Popen(["python", "/home/pi/led/progs10/hsv.py"])
					except:
						pass
					
			if data == "a1":
				try:
					if p.poll() == None:
						print "Can only start one process at a time"
				except:	
					try:
						p = subprocess.Popen(["python", "/home/pi/led/progs10/animation1.py"])
					except:
						pass
			
						
			if data == "snake":
				try:
					if p.poll() == None:
						print "Can only start one process at a time"
				except:
					try:
						#starte subprocess mit stdin für data weiterleitung
						p = subprocess.Popen(["python", "/home/pi/led/progs10/snake.py"], stdin=subprocess.PIPE)
						#stuff to communicate
						while data != "stop":
							data = client_sock.recv(1024)
							if len(data) == 0: 
								break
							#leite data an subprocess weiter
							p.stdin.write(data + "\n")
							p.stdin.flush()
							
					except:
						pass


			if data == "tetris":
				try:
					if p.poll() == None:
						print "Can only start one process at a time"
				except:
					try:
						#starte subprocess mit stdin für data weiterleitung
						p = subprocess.Popen(["python", "/home/pi/led/progs10/tetris.py"], stdin=subprocess.PIPE)
						#stuff to communicate
						while data != "stop":
							data = client_sock.recv(1024)
							if len(data) == 0: 
								break
							#leite data an subprocess weiter
							p.stdin.write(data + "\n")
							p.stdin.flush()
							
					except:
						pass


			if data == "scrollText":
				try:
					if p.poll() == None:
						print "Can only start one process at a time"
				except:
					try:
						#starte subprocess mit stdin für data weiterleitung
						p = subprocess.Popen(["python", "/home/pi/led/progs10/scrollText.py"], stdin=subprocess.PIPE)
						#stuff to communicate
						while data != "stop":
							data = client_sock.recv(1024)
							#if len(data) == 0: 
							#	break
							#leite data an subprocess weiter
							p.stdin.write(data + "\n")
							p.stdin.flush()
							
					except:
						pass
						
						
			if data == "color":
				try:
					if p.poll() == None:
						print "Can only start one process at a time"
				except:
					try:
						#starting subprocess with stdin
						p = subprocess.Popen(["python", "/home/pi/led/progs10/color.py"], stdin=subprocess.PIPE)
						#stuff to communicate
						while data != "stop":
							data = client_sock.recv(1024)
							if len(data) == 0: 
								break
							p.stdin.write(data + "\n")
							p.stdin.flush()
							
					except:
						pass


			#Clocks			
						
			if data == ("binClock"):
				try:
					if p.poll() == None:
						print "Can only start one process at a time"
				except:	
					try:
						#starte den subprocess und speichere ihn unter p
						p = subprocess.Popen(["python", "/home/pi/led/progs10/Clock.py", "binClock"])
					except:
						pass	
			if data == ("digClock"):
				try:
					if p.poll() == None:
						print "Can only start one process at a time"
				except:	
					try:
						#starte den subprocess und speichere ihn unter p
						p = subprocess.Popen(["python", "/home/pi/led/progs10/Clock.py", "digClock"])
					except:
						pass	

			if data == ("analogClock"):
				try:
					if p.poll() == None:
						print "Can only start one process at a time"
				except:	
					try:
						#starte den subprocess und speichere ihn unter p
						p = subprocess.Popen(["python", "/home/pi/led/progs10/Clock.py", "analogClock"])
					except:
						pass	

			if data == ("scrollClock"):
				try:
					if p.poll() == None:
						print "Can only start one process at a time"
				except:	
					try:
						#starte den subprocess und speichere ihn unter p
						p = subprocess.Popen(["python", "/home/pi/led/progs10/Clock.py", "scrollClock"])
					except:
						pass	




			


			if data == "black":
				try:
					subprocess.Popen(["python", "/home/pi/led/progs10/PiLed.py", "black"])
				except:
					pass
			
			if data == "smileyHappy":
				try:
					imgdisp("/home/pi/led/progs10/smiley-happy.png")
				except:
					pass
					
			if data == "smileySad":
				try:
					imgdisp("/home/pi/led/progs10/smiley-sad.png")
				except:
					pass
			
							
				
			if data == "stop":
				try:	
					p.kill()
					p = 0
					print "Process terminated"
				except:
					print "Unable to stop process"
					
	except IOError:
	# server Schleige abgebrochen. Stoppe laufenden Prozess zur Sicherheit.
		try:
			p.kill()
		except:
			pass
			
		#sad smiley face
		imgdisp("/home/pi/led/progs10/smiley-sad.png")
		time.sleep(1)
		imgdisp("/home/pi/led/progs10/black.png")
		pass
			
	print("disconnected")

	#schliesse client und server socket
	client_sock.close()
	server_sock.close()
	print("all done")
	
	
#unendliche while schleife sodass der Server bei einem Verbindungsabbruch
#automatisch nach 1 Sekunde neu startet.
while True:
	#LED's auf schwarz stellen
	subprocess.Popen(["python", "/home/pi/led/progs10/PiLed.py", "black"])
	#server funktion starten
	server()
	#warte 1 Sekunde damit Port 1 wieder frei ist und der Bluetooth Socket bereit ist
	time.sleep(1)


