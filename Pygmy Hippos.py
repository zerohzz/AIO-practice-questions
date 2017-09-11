# This program is on Python 2.7
# Answering the "Pygmy Hippos" problem
# AIO 2014 (Intermediate)
# http://orac.amt.edu.au/cgi-bin/train/problem.pl?set=aio14int&problemid=781

#Open input files
infile = open("hippoin.txt","r")

#Open output files
outfile = open("hippoout.txt","w")

#Read the input into the string, split by space
string1 = infile.read().split()
print string1

# the number of tulips
N = int(string1[0])
# position of first hippo
H1 = int(string1[1])
# position of second hippo
H2 = int(string1[2])
# position of third hippo
H3 = int(string1[3])

distances = []
# distance between first hippo and Starting point
d1 = H1 - 1
distances.append(d1)

# distance between first hippo and second hippo
d2 = H2 - H1 - 1
distances.append(d2)

# distance between second hippo and third hippo
d3 = H3 - H2 -1
distances.append(d3)

# distance between third hippo and last hippo
d4 = N - H3
distances.append(d4)

distances.sort()
print distances

#The output solution
solution = distances[2] + distances[3]

# write in the file
outfile.write(str(solution))

# Finally, close the input/output files.
infile.close()
outfile.close()

