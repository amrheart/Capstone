# this file will have two functions
# one will store data in as a new entry in the database
# one will retrieve a row (only one for now)
import sqlite3

# function one will store a list of formatted data in the database
def NewEntry(list_of_data):
	# whenever new entry is made, need to get total number of entries and increment
	file = open("SizeOfDb.txt", "r")
	row_num = file.readline()
	file.close()
	row_num = int(row_num)
	row_num = row_num + 1
	file = open("SizeOfDb.txt", "w")
	file.write(str(row_num))
	new_connection = sqlite3.connect("Capstone.db")
	cursor = new_connection.cursor()
	cursor.execute("INSERT INTO BikeTrip VALUES (" + str(row_num) + "," + str(list_of_data[0]) + "," + str(list_of_data[1]) + "," + str(list_of_data[2]) + "," + str(list_of_data[3]) + "," + str(list_of_data[4]) + ")")
	new_connection.commit()
	query2 = cursor.execute("SELECT * FROM BikeTrip")
	print(query2.fetchall())
	new_connection.close()

def GetRow(row_num):
	new_connection = sqlite3.connect("Capstone.db")
	cursor = new_connection.cursor()
	query = cursor.execute("SELECT * FROM BikeTrip WHERE TripID = " + str(row_num))
	row = query.fetchone()
	print(row)
	new_connection.close()
	return row

# utility function that grabs the last row in the database (most recent addtion)
def GetLastRow():
    db_num_file = open("SizeOfDb.txt", "r")
    row_num = db_num_file.readline()
    db_num_file.close()
    return GetRow(row_num)


# #cursor.execute("CREATE TABLE trip(speed, time, distance)")
# query = cursor.execute("SELECT name FROM sqlite_master")
# print(query.fetchone())
# cursor.execute("""INSERT INTO trip VALUES
# 	(40, 1, 4),
# 	(30, 2, 3)
# 	""")
# new_connection.commit()
# query2 = cursor.execute("SELECT time FROM trip")
# print(query2.fetchall())
# new_connection.close()
# input()

if __name__ == "__main__":
	#NewEntry([2,3,4])
	GetRow(1)
	GetLastRow()