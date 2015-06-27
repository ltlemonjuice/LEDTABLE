from bluetooth import *
import sys
import time

if sys.version < '3':
    input = raw_input

addr = "00:1A:7D:DA:71:13"

print("Trying to connect to LEDTABLE")

# search for the service
uuid = "94f39d29-7d6d-437d-973b-fba39e49d4aa"
service_matches = find_service( uuid = uuid, address = addr )

if len(service_matches) == 0:
	print("couldn't find the LEDTABLE service =(")
	time.sleep(2)
	sys.exit(0)

first_match = service_matches[0]
port = first_match["port"]
name = first_match["name"]
host = first_match["host"]

print("connecting to \"%s\" on %s" % (name, host))

# Create the client socket
sock=BluetoothSocket(RFCOMM)
sock.connect((host, port))

print("connected.  Please enter Commands:")
while True:
    data = input()
    if len(data) == 0: break
    sock.send(data)

sock.close()