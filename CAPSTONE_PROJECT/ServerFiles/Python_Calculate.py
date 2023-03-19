# this file holds functions to perform calculations on the trip data
import math
from Python_Helper import ClearFile
# function calculate speed will calculate the speed at every interval
def CalculateSpeed():
    C = 2 * math.pi
    ClearFile("data_with_speed_values.txt")
    
    # open the file of trip data
    data_set = open("TempDataStorage.txt", "r")
    output = open("data_with_speed_values.txt", "a")
    
    for line in data_set:
        washed_line = line.strip()
        values = washed_line.split(',')
        
        # calculate speed = C/interval
        speed = C/float(values[2])
        
        # write new line with speed value to output
        new_line = washed_line + "," + str(speed) + '\n'
        
        output.write(new_line)
        print(new_line)
        print(values)
        print(speed)
    data_set.close()
    output.close()
        
if __name__ == "__main__":
    CalculateSpeed()