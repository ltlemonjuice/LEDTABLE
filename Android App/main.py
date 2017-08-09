import kivy
kivy.require('1.0.9')
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.graphics import Color, Rectangle
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.screenmanager import ScreenManager, Screen
import time
from jnius import autoclass
from kivy.app import App
import os


#Lade mit dem Builder den kv language String
Builder.load_string('''
<FirstScreen>:
	GridLayout:
		cols: 1
		Label:
			size_hint_y: None
			height: 80
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
				text: "Chess"
				on_release:
					root.send("stop")
					root.send("chess")
					root.manager.current = "chessM"
					root.manager.transition.direction = "down"
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
			height: 80
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
			height: 160
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
			height: 160

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
			height: 80
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
			height: 160
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
				height: 80
				text: "Scrolling Text Controls"

			TextInput:
				id: ST
				size_hint_y: None
				height: 200
				multiline: False
				focus: False
				text: ""

			Button:
				size_hint_y: None
				height: 200
				text: "Display Text"
				on_release:
					root.send("*TEXT*%s" % ST.text)

			GridLayout:
				size_hint_y: None
				height: 100
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
				height: 400

				GridLayout:
					cols: 3
					size_hint_y: None
					height: 100
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
				height: 100
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
			height: 80
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
			height: 160
			Button:
				background_color: [2,0,0,1]
				text: 'Quit and Back to Menu'
				on_press:
					root.send("stop")
					root.send("black")
					root.manager.current = "1st"
					root.manager.transition.direction = "up"


<chessMain>:
	GridLayout:
		cols: 1
		Label:
			size_hint_y: None
			height: 100
			text: "Chess Controls"
		Button:
			text: "Play Mode"
			on_press:
				root.send("play")
				root.manager.current = "chessP"
				root.manager.transition.direction = "right"
		Button:
			text: "PGN Mode"
			on_press:
				root.send("pgn")
				root.manager.current = "chessp"
				root.manager.transition.direction = "left"
		GridLayout:
			cols: 1
			size_hint_y: None
			height: 160
			Button:
				background_color: [2,0,0,1]
				text: 'Quit and Back to Menu'
				on_press:
					root.send("stop")
					root.send("black")
					root.manager.current = "1st"
					root.manager.transition.direction = "up"

<chessPlay>:
	GridLayout:
		cols: 1
		Label:
			size_hint_y: None
			height: 100
			text: "Chess Play"
		TextInput:
			id: ST
			size_hint_y: None
			height: 50
			multiline: False
			focus: False
			text: ""

		Button:
			size_hint_y: None
			height: 160
			background_color: [0,1,0,1]
			text: "Make Move"
			on_release:
				root.send(ST.text)
				ST.text=""
		GridLayout:
			rows: 1
			Button:
				height: 160
				text: "R"
				on_release:
					ST.text += self.text
			Button:
				height: 160
				text: "N"
				on_release:
					ST.text += self.text
			Button:
				height: 160
				text: "B"
				on_release:
					ST.text += self.text
			Button:
				height: 160
				text: "Q"
				on_release:
					ST.text += self.text
			Button:
				height: 160
				text: "K"
				on_release:
					ST.text += self.text
			Button:
				height: 160
				background_color: [1,0,0,1]
				text: "DEL"
				on_release:
					ST.text = ST.text[:-1]
		GridLayout:
			rows: 1
			Button:
				height: 160
				text: "a"
				on_release:
					ST.text += self.text
			Button:
				height: 160
				text: "b"
				on_release:
					ST.text += self.text
			Button:
				height: 160
				text: "c"
				on_release:
					ST.text += self.text
			Button:
				height: 160
				text: "d"
				on_release:
					ST.text += self.text
			Button:
				height: 160
				text: "e"
				on_release:
					ST.text += self.text
			Button:
				height: 160
				text: "f"
				on_release:
					ST.text += self.text
			Button:
				height: 160
				text: "g"
				on_release:
					ST.text += self.text
			Button:
				height: 160
				text: "h"
				on_release:
					ST.text += self.text
		GridLayout:
			rows: 1
			Button:
				height: 160
				text: "1"
				on_release:
					ST.text += self.text
			Button:
				height: 160
				text: "2"
				on_release:
					ST.text += self.text
			Button:
				height: 160
				text: "3"
				on_release:
					ST.text += self.text
			Button:
				height: 160
				text: "4"
				on_release:
					ST.text += self.text
			Button:
				height: 160
				text: "5"
				on_release:
					ST.text += self.text
			Button:
				height: 160
				text: "6"
				on_release:
					ST.text += self.text
			Button:
				height: 160
				text: "7"
				on_release:
					ST.text += self.text
			Button:
				height: 160
				text: "8"
				on_release:
					ST.text += self.text
		GridLayout:
			rows: 1
			Button:
				height: 160
				text: "x"
				on_release:
					ST.text += self.text
			Button:
				height: 160
				text: "="
				on_release:
					ST.text += self.text
			Button:
				height: 160
				text: "O-O"
				on_release:
					ST.text += self.text
			Button:
				height: 160
				text: "O-O-O"
				on_release:
					ST.text += self.text
			Button:
				height: 160
				text: "+"
				on_release:
					ST.text += self.text
			Button:
				height: 160
				text: "#"
				on_release:
					ST.text += self.text
		GridLayout:
			rows: 1
			Button:
				height: 160
				text: "Show Pieces"
				on_release:
					root.send("showPieces")





		GridLayout:
			cols: 1
			size_hint_y: None
			height: 160
			Button:
				background_color: [2,0,0,1]
				text: 'Back'
				on_press:
					root.manager.current = "really"
					root.manager.transition.direction = "left"

<chessPGN>:
	id: PGN
	GridLayout:
		id: g1
		cols: 1
		Label:
			size_hint_y: None
			height: 100
			text: "Chess PGN"
		FileChooserListView:
			id: filechooser
			path: "/sdcard/Download/pgn/"

		GridLayout:
			cols: 1
			size_hint_y: None
			height: 160
			GridLayout:
				rows: 1
				Button:
					text: "Send"
					on_press:
						root.load(filechooser.path, filechooser.selection)
		GridLayout:
			cols: 1
			size_hint_y: None
			height: 160
			Button:
				background_color: [2,0,0,1]
				text: 'Back to Chess Main'
				on_press:
					root.send("reset")
					root.manager.current = "chessM"
					root.manager.transition.direction = "right"


<exitCheck>:
	GridLayout:
		cols: 1
		Label:
			text: "Really wanna cancel game?"
		GridLayout:
			rows: 1
			Button:
				text: "YES"
				on_press:
					root.manager.current = "chessM"

			Button:
				text: "NO"
				on_press:
					root.manager.current = "chessP"


''')


system = autoclass("java.lang.System")


class FirstScreen(Screen):

	checkState = False

	def connect(self):
		#set client variables and java classes
		adapter = autoclass("android.bluetooth.BluetoothAdapter")
		UUID = autoclass("java.util.UUID")
		pairedDevices = adapter.getDefaultAdapter().getBondedDevices().toArray()
		#sendStream wird global gesetzt damit man sie von anderen klassen aufrufen kann
		global sendStream
		global socket
		#connecting
		#checkt ob checkState bereits True ist
		if self.checkState == False:
			for device in pairedDevices:
				system.out.println(device.getName())
				if device.getName() == "LED-TABLE_v1.0":
					try:
						id = "94f39d29-7d6d-437d-973b-fba39e49d4aa"
						socket = device.createRfcommSocketToServiceRecord(UUID.fromString(id))
						sendStream = socket.getOutputStream()
						system.out.println("try to connect")
						socket.connect()
						self.checkState = True
						system.out.println("connected")

					except:
						system.out.println("unsuccessful")
						self.checkState = False

					break
		else:
			if socket.isConnected():
				system.out.println("already connected!")
			else:
				self.checkState = False
				connect()


	def setTime(self):
		timeSET = "TIME " + time.ctime()
		try:
			sendStream.write(timeSET)
			sendStream.flush()
		except:
			system.out.println("not yet connected")

	def send(self, data):
		try:
			sendStream.write(data)
			sendStream.flush()
			system.out.println("Sent: " + data)
		except:
			system.out.println("not yet connected")


class SecondScreen(Screen):
	def send(self, data):
		try:
			sendStream.write(data)
			sendStream.flush()
			system.out.println("Sent: " + data)
		except:
			system.out.println("not yet connected")


class ThirdScreen(Screen):
	def send(self, data):
		try:
			sendStream.write(data)
			sendStream.flush()
			system.out.println("Sent: " + data)
		except:
			system.out.println("not yet connected")

class FourthScreen(Screen):
	def send(self, data):
		try:
			sendStream.write(data)
			sendStream.flush()
			system.out.println("Sent: " + data)
		except:
			system.out.println("not yet connected")


class FifthScreen(Screen):
	def send(self, data):
		try:
			sendStream.write(data)
			sendStream.flush()
			system.out.println("Sent: " + data)
		except:
			print("not yet connected")

class SixthScreen(Screen):
	def send(self, data):
		try:
			sendStream.write(data)
			sendStream.flush()
			system.out.println("Sent: " + data)
		except:
			print("not yet connected")

class chessMain(Screen):
	def send(self, data):
		try:
			sendStream.write(data)
			sendStream.flush()
			system.out.println("Sent: " + data)
		except:
			print("not yet connected")

class chessPlay(Screen):

	toSend = ""



	def send(self, data):
		try:
			sendStream.write(data)
			sendStream.flush()
			system.out.println("Sent: " + data)
		except:
			print("not yet connected")



class chessPGN(Screen):

	def load(self, path, filename):
		string=""
		try:
			f = open(os.path.join(path, filename[0]), "r")
			string = f.read().replace("\n", " ")
			self.send(string)
		except:
			pass


	def send(self, data):
		try:
			sendStream.write(data)
			sendStream.flush()
			system.out.println("Sent: " + data)
		except:
			print("not yet connected")


class exitCheck(Screen):
	def send(self, data):
		try:
			sendStream.write(data)
			sendStream.flush()
			system.out.println("Sent: " + data)
		except:
			system.out.println("not yet connected")


sm = ScreenManager()
sm.add_widget(FirstScreen(name="1st"))
sm.add_widget(SecondScreen(name="2nd"))
sm.add_widget(ThirdScreen(name="3rd"))
sm.add_widget(FourthScreen(name="4th"))
sm.add_widget(FifthScreen(name="5th"))
sm.add_widget(SixthScreen(name="6th"))
sm.add_widget(chessMain(name="chessM"))
sm.add_widget(chessPlay(name="chessP"))
sm.add_widget(chessPGN(name="chessp"))
sm.add_widget(exitCheck(name="really"))



class GUI(App):
	def on_pause(self):
		return True

	def build(self):
		return sm

if __name__ == '__main__':
	GUI().run()
