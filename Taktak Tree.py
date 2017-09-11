# This program is on Python 2.7
# Answering the "The Tremendous Tak-Tak Tree" problem
# http://orac.amt.edu.au/cgi-bin/train/problem.pl?set=simple2&problemid=382

import sys

#Open input files
infile = open("taktakin.txt","r")

#Open output files
outfile = open("taktakout.txt","w")

#Read the input into the string, split by space
string1 = infile.read().split()
print string1

days = 0
fruit = int(string1[0])


while (fruit % 11 != 1):
    fruit = fruit * 2
    days = days + 1


#The output solution
solution = str(days) + " " + str(fruit)
#write in the file
outfile.write(str(solution))

# Finally, close the input/output files.
infile.close()
outfile.close()
