# utility functions for python

# function will clear the specified file
def ClearFile(file):
    opened_for_clearing = open(file, "a")
    opened_for_clearing.truncate(0)