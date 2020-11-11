# initialize my data variableo
data = []

# Read and parse the data file
filename = "data/wxobs20170821.txt"

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

#for datum in data[slice(0,10,2)]:
for datum in data:
  print(datum)
