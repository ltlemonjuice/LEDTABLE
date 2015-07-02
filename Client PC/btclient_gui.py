#imports
from bluetooth import *
import kivy
import sys
import time

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.slider import Slider
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.screenmanager import ScreenManager, Screen


#Lade mit dem Builder den kv language String
Builder.load_string('''
<FirstScreen>:
	GridLayout:
		cols: 1
		Label:
			size_hint_y: None
			height: 20
			text: 'LED TABLE GUI'
		Button:
			background_color: [0,0,2,1]
			text: "Connect to Table"
			on_release:
				root.connect()

		Button:
			text: "Clock"
			on_release:
				root.send("stop")
				root.setTime()
				root.manager.current = "6th"
				root.manager.transition.direction = "down"
		
		Button:
			text: "Scrolling Text"
			on_release:
				root.send("stop")
				root.send("scrollText")
				root.manager.current = "5th"
				root.manager.transition.direction = "up"

		Button:
			text: 'HSV'
			on_release:
				root.send("stop")
				root.send("hsv")
		Button:
			text: 'Animation 1'
			on_release:
				root.send("stop")
				root.send("a1")
		GridLayout:
			rows: 1
			Button:
				text: "Snake"
				on_release:
					root.send("stop")
					root.send("snake")
					root.manager.current = "2nd"
					root.manager.transition.direction = "left"
			Button:
				text: "Tetris"
				on_release:
					root.send("stop")
					root.send("tetris")
					root.manager.current = "4th"
					root.manager.transition.direction = "left"
		Button:
			text: "Custom Color"
			on_release:
				root.send("stop")
				root.send("color")
				root.manager.current = "3rd"
				root.manager.transition.direction = "right"
		GridLayout:
			cols: 2
			Button:
				background_color: [2,0,0,1]
				text: 'Stop'
				on_release:
					root.send("stop")
			Button:
				background_color: [0.5,0.5,0.5,1]
				text: 'Turn Black'
				on_release:
					root.send("black")



<SecondScreen>:
	GridLayout:
		cols: 1
		Label:
			size_hint_y: None
			height: 20
			text: "Snake Controls"

		Button:
			text: "Up"
			on_release:
				root.send("up")

		GridLayout:
			cols: 3
			rows: 1
			Button:
				text: "Left"
				on_release:
					root.send("left")
			Button:
				text: "Down"
				on_release:
					root.send("down")
			Button:
				text: "Right"
				on_release:
					root.send("right")

		GridLayout:
			cols: 1	
			size_hint_y: None
			height: 20
			Button:
				background_color: [2,0,0,1]
				text: 'Quit and Back to Menu'
				on_press: 
					root.send("stop")
					root.send("black")
					root.manager.current = "1st"
					root.manager.transition.direction = "right"

<ThirdScreen>:
	GridLayout:
		cols: 1

		ColorPicker:
			id: CP

		GridLayout:
			rows: 1
			size_hint_y: None
			height: 40

			Button:
				text: "Set Color"
				on_release:
					root.send("[" + str(int(CP.color[0]*255)) + ", " + str(int(CP.color[1]*255)) + ", " + str(int(CP.color[2]*255)) + "]")
					

			Button:
				background_color: [2,0,0,1]
				text: "Quit and Back to Menu"
				on_release:
					root.send("stop")
					root.manager.current = "1st"
					root.manager.transition.direction = "left" 
					
<FourthScreen>:
	GridLayout:
		cols: 1
		Label:
			size_hint_y: None
			height: 20
			text: "Tetris Controls"

		Button:
			text: "Turn"
			on_release:
				root.send("turn")

		GridLayout:
			cols: 3
			rows: 1
			Button:
				text: "Left"
				on_release:
					root.send("left")
			Button:
				text: "Down"
				on_release:
					root.send("down")
			Button:
				text: "Right"
				on_release:
					root.send("right")

		GridLayout:
			cols: 1	
			size_hint_y: None
			height: 40
			Button:
				background_color: [2,0,0,1]
				text: 'Quit and Back to Menu'
				on_press: 
					root.send("stop")
					root.send("black")
					root.manager.current = "1st"
					root.manager.transition.direction = "right"

<FifthScreen>:
	AnchorLayout:
		GridLayout:
			anchor_x: "center"
			anchor_y: "top"	
			cols: 1
			Label:
				size_hint_y: None
				height: 20
				text: "Scrolling Text Controls"
			
			TextInput:
				id: ST
				size_hint_y: None
				height: 40
				multiline: False
				focus: False
				text: ""
		
			Button:
				size_hint_y: None
				height: 40
				text: "Display Text"
				on_release:
					root.send(ST.text)

			GridLayout:
				size_hint_y: None
				height: 40
				cols: 2
				Slider:
					id: SPSL
					min: 0
					max: 0.1
					value: 0.025
					step: 0.001
				Button:
					text: "Set Speed to %s" % SPSL.value
					on_release:
						root.send("*SPEED*%s" %SPSL.value)

			
			GridLayout:
				rows: 2
				size_hint_y: None
				height: 200
				
				GridLayout:
					cols: 3
					size_hint_y: None
					height: 20
					Label:
						text: "Red"
					Label:
						text: "Green"
					Label:
						text: "Blue"

				GridLayout:
					cols: 3	

					Slider:
						id: red
						orientation: "vertical"
						min: 0
						max: 255
						value: 255
						step: 1
					Slider:
						id: green
						orientation: "vertical"
						min: 0
						max: 255
						value: 0
						step: 1
					Slider:
						id: blue
						orientation: "vertical"
						min: 0
						max: 255
						value: 0
						step: 1

					


			Button:
				size_hint_y: None
				height: 40
				text: "Set Color"
				on_release:
					root.send("*COLOR*["+ str(int(red.value)) + "," + str(int(green.value)) + "," + str(int(blue.value))+ "]")


			

		

		

	
	Button:
		size_hint_y: None
		height: 160
		anchor_x: "center"
		anchor_y: "bottom"	
		background_color: [2,0,0,1]
		text: 'Quit and Back to Menu'
		on_press: 
			root.send("stop")
			root.send("black")
			root.manager.current = "1st"
			root.manager.transition.direction = "down"

<SixthScreen>:
	GridLayout:
		cols: 1
		Label:
			size_hint_y: None
			height: 20
			text: "Clock Controls"

		GridLayout:
			cols: 2
			rows: 2
			Button:
				text: "Binary Clock"
				on_release:
					root.send("stop")
					root.send("binClock")
			Button:
				text: "Digital Clock"
				on_release:
					root.send("stop")
					root.send("digClock")

			Button:
				text: "Analog Clock"
				on_release:
					root.send("stop")
					root.send("analogClock")
			Button:
				text: "Scrolling Clock"
				on_release:
					root.send("stop")
					root.send("scrollClock")

			

		GridLayout:
			cols: 1	
			size_hint_y: None
			height: 40
			Button:
				background_color: [2,0,0,1]
				text: 'Quit and Back to Menu'
				on_press: 
					root.send("stop")
					root.send("black")
					root.manager.current = "1st"
					root.manager.transition.direction = "up"
''')




class FirstScreen(Screen):
	global checkState
	checkState = False
	

	def connect(self):
		global checkState
		global sock
		##connect to Server
		addr = "00:1A:7D:DA:71:13"
		uuid = "94f39d29-7d6d-437d-973b-fba39e49d4aa"
		sock = BluetoothSocket(RFCOMM)
		if checkState == False:
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

			port = int(raw_input("Port (1-3)? "))

			sock.connect((host, port))
			print("connected")

			checkState = True


	def setTime(self):
		timeSET = "TIME " + time.ctime()
		#try:
		sock.send(timeSET)
		#except:
		#	print("not yet connected")
		
	def send(self, data):
		try:
			sock.send(data)
			print("Sent: " + data)
		except:
			print("not yet connected")


class SecondScreen(Screen):
	def send(self, data):
		try:
			sock.send(data)
			print("Sent: " + data)
		except:
			print("not yet connected")


class ThirdScreen(Screen):
	def send(self, data):
		try:
			sock.send(data)
			print("Sent: " + data)
		except:
			print("not yet connected")
			
class FourthScreen(Screen):
	def send(self, data):
		try:
			sock.send(data)
			print("Sent: " + data)
		except:
			print("not yet connected")

class FifthScreen(Screen):
	def send(self, data):
		try:
			sock.send(data)
			print("Sent: " + data)
		except:
			print("not yet connected")
	
class SixthScreen(Screen):
	def send(self, data):
		try:
			sock.send(data)
			print("Sent: " + data)
		except:
			print("not yet connected")
	
	

	
sm = ScreenManager()
sm.add_widget(FirstScreen(name="1st"))
sm.add_widget(SecondScreen(name="2nd"))
sm.add_widget(ThirdScreen(name="3rd"))
sm.add_widget(FourthScreen(name="4th"))
sm.add_widget(FifthScreen(name="5th"))
sm.add_widget(SixthScreen(name="6th"))
				
class GUI(App):
	def on_pause(self):
		return True

	def build(self):
		return sm

if __name__ == '__main__':
	GUI().run()