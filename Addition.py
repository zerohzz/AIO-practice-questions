# This program is on Python 2.7
# Answering the "Addition" problem
# http://orac.amt.edu.au/cgi-bin/train/problem.pl?set=simple1&problemid=333

import sys

# Open input files
infile = open("addin.txt","r")

# Open output files
outfile = open("addout.txt","w")

# Read the input into the string, split by space
string1 = infile.read().split()

# number 1 = first item in string, number 2 = second one
number1 = int(string1[0])
number2 = int(string1[1])

# sum two number
sum = number1 + number2

# write in the file
outfile.write(str(sum))

# Finally, close the input/output files.
infile.close()
outfile.close()

