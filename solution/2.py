infile = open("addin.txt","r")
string1 = infile.read().split()

outfile = open("addout.txt","w")

string2 = str(int(string1[0]) + int(string1[1]))
outfile.write(string2)