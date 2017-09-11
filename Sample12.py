#Open input files
infile = open("probein.txt","r")

#Open output files
outfile = open("probeout.txt","w")

#Read the input into the string, split by space
string1 = infile.read().split()
print string1

# Read the first line
row = int(string1[0])
column = int(string1[1])
rowP = int(string1[2])
colP = int(string1[3])
rowF = int(string1[4])
colF = int(string1[5])
question = int(string1[6])

i = 7
while i < (question*2)+6:
    x = int(string1[i])
    y = int(string1[i+1])

    if abs(rowP-rowF) == abs(colP-colF):
        water = max(abs(rowP-x),abs(colP-y))
        lava = max(abs(rowF-x),abs(colF-y))
    else:
        water = abs(rowP-x) + abs(colP-y)
        lava = abs(rowF-x) + abs(colF-y)

    #write in the file
    if water == lava:
        outfile.write("MOUNTAINS\n")
    elif water < lava:
        outfile.write("WATER\n")
    else:
        outfile.write("LAVA\n")

    i += 2

# Finally, close the input/output files.
infile.close()
outfile.close()
