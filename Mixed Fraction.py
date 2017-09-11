# This program is on Python 2.7
# Answering the "Mixed Fraction" problem
# http://orac.amt.edu.au/cgi-bin/train/problem.pl?set=simple1&problemid=362

import sys

def min(a,b):
  if (a<b):
    return a
  else:
    return b

def max(a,b):
  if (a>b):
    return a
  else:
    return b


#Open input files
infile = open("mixin.txt","r")

#Open output files
outfile = open("mixout.txt","w")

#Read the input into the string, split by space
string1 = infile.read().split()

#Read numbers
left_1 = int(string1[0])
bottom_1 = int(string1[1])
right_1 = int(string1[2])
top_1 = int(string1[3])

left_2 = int(string1[4])
bottom_2 = int(string1[5])
right_2 = int(string1[6])
top_2 = int(string1[7])

#Calculate the intersection co-ordinates.
inter_left = max(left_1,left_2)
inter_bottom = max(bottom_1,bottom_2)
inter_right = min(right_1,right_2)
inter_top = min(top_1,top_2)

#Calculate the areas of the rectangles and the intersection.
area_1 = (right_1 - left_1) * (top_1 - bottom_1)
area_2 = (right_2 - left_2) * (top_2 - bottom_2)

if inter_left < inter_right and inter_bottom < inter_top:
    inter_area = (inter_right - inter_left) * (inter_top - inter_bottom)
else:
    inter_area = 0

#The output solution
total_area = area_1 + area_2 - inter_area

#write in the file
outfile.write(str(total_area))

# Finally, close the input/output files.
infile.close()
outfile.close()
