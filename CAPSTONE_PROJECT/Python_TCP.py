# using tCP for connecting with pi, might need to use CAP

import socket

# will wait for data to be sent by iot device, then post it to outputfile
def GetData():
	Host = ''
	Port = 50001
	# listen for iot device
	new_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	new_sock.bind((Host, Port))
	new_sock.listen(1)
	conn_data = new_sock.accept()
	connection = conn_data[0]
	address = conn_data[1]
	print("User ", address)

	file = open("TempDataStorage.txt", "a")
	file.truncate(0)
	while True:
		data = connection.recv(1024)
		if not data: break
		data = str(data)
		data = data.strip('b')
		data = data.strip('"')
		data = data.strip("'")
		print(data)
		file.write(data + "\n")
	file.close()
	connection.close()

if __name__ == "__main__":
	GetData()