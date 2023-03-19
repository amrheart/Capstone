# This program will facilitate the server of the bike trip program
# will be able to recieve data from the iot device
# will be able to process the data and turn it into a graph
# after manipulating data, will be able to insert it into a table

from Python_TCP import GetData
from Python_DB import NewEntry
from Python_Calculate import CalculateSpeed
import socket
import math
whee_size = 5

# will loop indefintely
while True:
	# wait for data to come in from iot device
	GetData()
	CalculateSpeed()

	# perform manipulations on the data
	# need only the first and last entries for now
	last_line = ""
	first_line = ""
	file = open("data_with_speed_values.txt", "r")
	all_lines = file.readlines()
	file.close()
	first_line = all_lines[0]
	last_line = all_lines[-1]
	last_line = last_line.rstrip()
	print(last_line)
	data = last_line.split(",")
	print(first_line)
	print(last_line)

	# Trip time is the second value in data
	trip_distance = float(data[1]) * 2 * math.pi

	# get temperature data
	file = open("TemperatureStorage.txt", "r")
	temp_data = file.readlines()
	begin_temp = temp_data[0]
	end_temp = temp_data[1]
	begin_temp = begin_temp.rstrip()
	begin_temp = begin_temp.split(",")
	end_temp = end_temp.rstrip()
	end_temp = end_temp.split(",")

	# store data in table as an entry
	print(data)
	new_data = [data[3], data[1], trip_distance, begin_temp[0], end_temp[0]]
	NewEntry(new_data)

	# print entry to console as query

