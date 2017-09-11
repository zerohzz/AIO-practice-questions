# This program is on Python 2.7
# Answering the "A Dish Best Served Cold" problem
# http://orac.amt.edu.au/cgi-bin/train/problem.pl?set=simple2&problemid=397

#Open input files
infile = open("dishin.txt","r")

#Open output files
outfile = open("dishout.txt","w")

#Read the input into the string, split by space
string1 = infile.read().split()
print string1

# size of dataset
size = int(string1[0])

min =  999999999
max = -999999999
sum = 0

for i in range(1,size+1):
    tmp = int(string1[i])
    if min > tmp:
        min = tmp
    if max < tmp:
        max = tmp
    sum += tmp


#The output solution

solution = str(min) + " " + str(max) + " " + str(sum/size)
#write in the file
outfile.write(str(solution))

# Finally, close the input/output files.
infile.close()
outfile.close()
