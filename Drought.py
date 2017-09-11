# This program is on Python 2.7
# Answering the "Drought" problem
# http://orac.amt.edu.au/cgi-bin/train/problem.pl?set=simple2&problemid=398

#Open input files
infile = open("rainin.txt","r")

#Open output files
outfile = open("rainout.txt","w")

#Read the input into the string, split by space
string1 = infile.read().split()
print string1

# Read the first line
days = int(string1[0])
capacity = int(string1[1])

total = 0
for day in range(2,days+2):
    rain = int(string1[day])
    total += rain
    if total >= capacity:
        #The output solution
        outfile.write(str(day-1))
        break

# Finally, close the input/output files.
infile.close()
outfile.close()
