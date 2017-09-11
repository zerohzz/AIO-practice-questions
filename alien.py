# Alien
# AIO 2011
# Python Sample Solution

# These are the limits as defined in the problem statement.
MAX_HUMANS = 100000
MAX_WIDTH = 1000000

# n is the number of humans.
n = None

# w is the width of the beam.
w = None

# The p[] array will contain the positions of each of the humans, as described
# in the problem statement. The first position is stored in p[0].
p = [None for x in range(MAX_HUMANS)]

# Open the input and output files.
inputFile = open("alienin.txt", "r")
outputFile = open("alienout.txt", "w")

# Read the values of N and W from the input file. 
input_line = inputFile.readline().strip()
n, w = [int(x) for x in input_line.split()]

# Read the values of p_i into the p array.
for i in range(0, n):
    p[i] = int(inputFile.readline().strip())

# Calculate the answer.
answer = 0
first = 0
last = 0

for last in range(n):
    while p[last]-p[first] >= w:
        first += 1
    if answer < last - first + 1:
        answer = last - first + 1

# Write the answer to the output file.
outputFile.write(str(answer))

# Finally, close the input/output files.
inputFile.close()
outputFile.close()
