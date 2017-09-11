# This program is on Python 2.7
# Answering the "Encyclopædia" problem
# http://orac.amt.edu.au/cgi-bin/train/problem.pl?set=simple3&problemid=412

#Open input files
infile = open("in.txt","r")

#Open output files
outfile = open("out.txt","w")

#Read the input into the string, split by space
string1 = infile.read().split()
print string1

# Read the first line
n = int(string1[0])
q = string1[1]

# Read in the list of pages
pages = []
questions = []
solution = []
for i in range(2,n+2):
    pages.append(string1[i])

for x in range(n+2,len(string1)):
    questions.append(string1[x])

#write in the file
#The output solution
for j in questions:
    outfile.write(pages[int(j)-1] + "\n")

# Finally, close the input/output files.
infile.close()
outfile.close()
