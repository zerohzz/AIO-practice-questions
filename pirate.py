
# Pirates
# AIO 2011
# Python Sample Solution

# Open the input and output files.
inputFile = open("piratein.txt", "r")
outputFile = open("pirateout.txt", "w")

# Read the input.
myInput = inputFile.read().split()
l = int(myInput[0])
x = int(myInput[1])
y = int(myInput[2])

# Calculate the answer.
ans = min(x+y, 2*l-x-y)

# Write the answer to the output file.
outputFile.write(str(ans)+"\n")

# Finally, close the input/output files.
inputFile.close()
outputFile.close()
