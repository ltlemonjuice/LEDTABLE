#imports
from bluetooth import *
import sys
import time

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen

#connect to Server
addr = "00:1A:7D:DA:71:13"
uuid = "94f39d29-7d6d-437d-973b-fba39e49d4aa"
sock=BluetoothSocket(RFCOMM)

print("Trying to connect to LEDTABLE")
service_matches = find_service( uuid = uuid, address = addr )

if len(service_matches) == 0:
	print("couldn't find the LEDTABLE service =(")
	time.sleep(1)
	sys.exit(0)

first_match = service_matches[0]
port = first_match["port"]
name = first_match["name"]
host = first_match["host"]

print("connecting to \"%s\" on %s" % (name, host))

sock.connect((host, port))
print("connected")

	




#Actual App
class Client(App):
	
	def send(self, data):
		sock.send(data)
	
	def hsv(self, instance):
		self.send("hsv")

	def a1(self, instance):
		self.send("a1")

	def stop(self, instance):
		self.send("stop")
			
	def black(self, instance):
		self.send("black")

		
	def build(self):
		g = GridLayout(rows=5, cols=0)
		button = Button(text="HSV")
		button2 = Button(text="Animation 1")
		button3 = Button(text="Stop")
		button4 = Button(text="Turn Black")
		g.add_widget(button)
		g.add_widget(button2)
		g.add_widget(button3)
		g.add_widget(button4)
		
		button.bind(on_press=self.hsv)
		button2.bind(on_press=self.a1)
		button3.bind(on_press=self.stop)
		button4.bind(on_press=self.black)
		
		return g
	
if __name__ == "__main__":
	Client().run()
	
	

