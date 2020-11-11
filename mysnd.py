# Read the data file downloaded from ...

# initialize my data variableo

data = []

filename = "data/wxobs20170821.txt"

# in place of above 3 lines, one can do

with open(filename, 'r') as datafile:

# read the first three lines (header)
 for _ in range(3):
    datafile.readline()
#   print(_)

# read and parse the rest of the file
 for line in datafile:
    datum = line.split()
    data.append(datum)

# DEBUG
#print(data[8][4])
#print(data[8][:5])
#print(data[8][::2])
#print(data[0:10])
#print(data[9])
#print(data[-1])
# check data type (for this one, it is 'str')
# print(type(data))
# print(data)

#for datum in data[slice(0,10,2)]:
for datum in data:
  print(datum)
