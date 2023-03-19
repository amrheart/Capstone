# program should be run once to set up database tables
# run sql code to setup tables

import sqlite3
from Python_Helper import ClearFile

db_name = "Capstone.db"
new_connection = sqlite3.connect(db_name)
cursor = new_connection.cursor()
cursor.execute("DROP TABLE BikeTrip")
cursor.execute("CREATE TABLE Biketrip(TripID, AverageSpeed, TripTime, TripDistance, StartTemp, EndTemp)")
print("New table BikeTrip created in " + db_name)
# open size of database and set to 0
file = "SizeOfDb.txt"
ClearFile(file)
open_file = open(file, "w")
open_file.write("0")

print("Test to see if its working: ")
query = cursor.execute("SELECT name FROM sqlite_master")
print(query.fetchone())

new_connection.close()
input()