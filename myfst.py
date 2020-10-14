
# 1.
#print("Hello, World!")

# Read the data file downloaded from ...

# 2.
filename = "data/wxobs20170821.txt"
#datafile = open(filename,'r')

# read the first 4 lines
#print(datafile.readline())
#print(datafile.readline())
#print(datafile.readline())
#print(datafile.readline())

#datafile = open(filename,'r')
#data = datafile.read()
#datafile.close()

# in place of above 3 lines, one can do

with open(filename, 'r') as datafile:
    data = datafile.read()

# DEBUG
# check data type (for this one, it is 'str')
# print(type(data))
# print(data)

