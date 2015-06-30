import kivy
kivy.require('1.0.9')
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
import time
from jnius import autoclass
from kivy.app import App
import time


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
			text: "Binary Clock"
			on_release:
				root.send("stop")
				root.send("binClock")
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
					
					break
		else:
			system.out.println("already connected!")
		
	def send(self, data):
		try:
			sendStream.write(data)
			sendStream.flush()
		except:
			system.out.println("not yet connected")


class SecondScreen(Screen):
	def send(self, data):
		try:
			sendStream.write(data)
			sendStream.flush()
		except:
			system.out.println("not yet connected")


class ThirdScreen(Screen):
	def send(self, data):
		try:
			sendStream.write(data)
			sendStream.flush()
		except:
			system.out.println("not yet connected")
			
class FourthScreen(Screen):
	def send(self, data):
		try:
			sendStream.write(data)
			sendStream.flush()
		except:
			system.out.println("not yet connected")
	
	
	
	
	
	
sm = ScreenManager()
sm.add_widget(FirstScreen(name="1st"))
sm.add_widget(SecondScreen(name="2nd"))
sm.add_widget(ThirdScreen(name="3rd"))
sm.add_widget(FourthScreen(name="4th"))
				
class GUI(App):
	def on_pause(self):
		return True

	def build(self):
		return sm

if __name__ == '__main__':
	GUI().run()
