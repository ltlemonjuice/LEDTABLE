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

#lade mit dem Builder den kv language String
Builder.load_string('''
<FirstScreen>:
	GridLayout:
		cols: 1
		Label:
			text: 'LEDTABLE CONTROL CENTER'
		
		Button:
			text: "Connect to Table"
			on_release:
				root.connect()
		Button:
			text: 'HSV'
			on_release:
				root.send("hsv")
		Button:
			text: 'Animation 1'
			on_release:
				root.send("a1")
		Button:
			text: "Costum Color"
			on_release:
				root.send("color")
				root.manager.current = "3rd"
				root.manager.transition.direction = "right"
		Button:
			text: "Snake"
			on_release:
				root.send("snake")
				root.manager.current = "2nd"
				root.manager.transition.direction = "left"
		GridLayout:
			cols: 2
			Button:
				text: 'Stop'
				on_release:
					root.send("stop")
			Button:
				text: 'Turn Black'
				on_release:
					root.send("black")
		


<SecondScreen>:
	GridLayout:
		cols: 1
		Label:
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
			Button:
				text: 'Quit and Back to Menu'
				on_press: 
					root.send("stop")
					root.send("black")
					root.manager.current = "1st"
					root.manager.transition.direction = "right"

<ThirdScreen>:
	GridLayout:
		cols: 1
		Label:
			text: "Color Picker"
		Label:
			text: 'Red: ' + str(int(SliderR.value))
		Slider:
			id: SliderR
			min: 0
			max: 255
			step: 1
			padding: 100
		Label:
			text: "Green: " + str(int(SliderG.value))
		Slider:
			id: SliderG
			min: 0
			max: 255
			step: 1
			padding: 100
		Label:
			text: "Blue: " + str(int(SliderB.value))
		Slider:
			id: SliderB
			min: 0
			max: 255
			step: 1
			padding: 100
		Button:
			text: "Set Color"
			on_release:
				#Send RGB Values as list in String
				root.send("[" + str(int(SliderR.value)) + ", " + str(int(SliderG.value)) + ", " + str(int(SliderB.value)) + "]")

		Button:
			text: "Quit and Back to Menu"
			on_release:
				root.send("stop")
				root.manager.current = "1st"
				root.manager.transition.direction = "left"
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
	
	
	
	
	
	
sm = ScreenManager()
sm.add_widget(FirstScreen(name="1st"))
sm.add_widget(SecondScreen(name="2nd"))
sm.add_widget(ThirdScreen(name="3rd"))
				
class GUI(App):
	def on_pause(self):
		return True

	def build(self):
		return sm

if __name__ == '__main__':
	GUI().run()