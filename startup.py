import time
import array
import fcntl

spidev = file("/dev/spidev0.0", "wb")
#byte array to store rgb values
rgb=bytearray(3)
#setting spi frequency to 400kbps
fcntl.ioctl(spidev, 0x40046b04, array.array('L', [400000]))

#for Schleife für die rot Werte 1-255)
for x in range(1, 256):
	#langsam den rot wert steigern und anzeigen
	for i in range(0, 100):
		rgb[0] = int(x)
		rgb[1] = int(0)
		rgb[2] = int(0)
		spidev.write(rgb)
	spidev.flush()

time.sleep(1)

#Alle LED's wieder auf schwarz setzen
for i in range(0, 100): 
	rgb[0] = int(0)
	rgb[1] = int(0)
	rgb[2] = int(0)
	spidev.write(rgb)
spidev.flush()