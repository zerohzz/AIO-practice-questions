# This program is on Python 2.7
# Answering the "Sitting or Standing?" problem
# http://orac.amt.edu.au/cgi-bin/train/problem.pl?set=simple1&problemid=342

#Open input files
infile = open("sitin.txt","r")

#Open output files
outfile = open("sitout.txt","w")

#Read the input into the string, split by space
string1 = infile.read().split()


#Read numbers
row = int(string1[0])
seat = int(string1[1])
ticket = int(string1[2])

#The output solution
solution1 = row * seat
solution2 = ticket - row*seat

#write in the file
outfile.write(str(solution1)+" " + str(solution2))

# Finally, close the input/output files.
infile.close()
outfile.close()
