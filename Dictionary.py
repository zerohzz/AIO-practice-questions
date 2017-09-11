# This program is on Python 2.7
# Answering the "Dictionary" problem
# http://orac.amt.edu.au/cgi-bin/train/problem.pl?set=simple3&problemid=413

#Open input files
infile = open("dictin.txt","r")

#Open output files
outfile = open("dictout.txt","w")

#Read the input into the string, split by space
string1 = infile.read().split()
print string1

# Read the first line
# word = number of words
# queries = number of translation
words = int(string1[0])
queries = int(string1[1])

# dictionary 1 for Integerlandese
# dictionary 2 for Wholenumberlandese
dict_1 = []
dict_2 = []

# append word for two dictionary
i = 2
while i <= words*2 :
    dict_1.append(string1[i])
    dict_2.append(string1[i+1])
    i+=2

w_lines = int(words*2 + 2)
word_list = []

# start translation
for i in range(w_lines,w_lines+queries):
    found = False
    for j in range(words):
        if dict_1[j] == string1[i]:
            word_list.append(dict_2[j])
            found = True
    if found == False:
        word_list.append("C?")

for i in range(len(word_list)):
    outfile.write(word_list[i] + "\n")


#write in the file
#The output solution

#outfile.write(pages[int(j)-1] + "\n")

# Finally, close the input/output files.
infile.close()
outfile.close()

