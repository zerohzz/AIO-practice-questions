# Oil
# AIO 2010
# Python Sample Solution

# These are the limits as defined in the problem statement.
MAX_R = 2000
MAX_C = 2000

# num_rows and num_cols will contain the height and width of the map,
# respectively.
num_rows = None
num_cols = None

# num_days will contain the number of days that you need to perform the
# simulation.
num_days = None

grid = [[[None for x in xrange(MAX_C)] for x in xrange(MAX_R)] for x in xrange(2)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# Open the input and output files.
inputFile = open("oilin.txt", "r")
outputFile = open("oilout.txt", "w")

# Read the height and width of the map from the input file, and the number of
# days to simulate for.
input_line = inputFile.readline().strip()
num_rows, num_cols, num_days = [int(x) for x in input_line.split()]
for r in xrange(num_rows):
    # Read the next row of the map.
    input_str = inputFile.readline().strip()

    # Copy the row we just read into the map.
    for c in xrange(num_cols):
        grid[0][r][c] = input_str[c]

# Find the spill
def colour(day, r, c):
    if r < 0 or c < 0 or r >= num_rows or c >= num_cols:
        return
    if grid[(day+1)%2][r][c] != '.':
        return
    grid[day%2][r][c] = '*'
    return

for d in xrange(num_days):
    for r in xrange(num_rows):
        for c in xrange(num_cols):
            grid[(d+1)%2][r][c] = grid[d%2][r][c]
    for r in xrange(num_rows):
        for c in xrange(num_cols):
            if grid[d%2][r][c] == '*' or grid[d%2][r][c] == '$':
                for i in xrange(4):
                    colour(d+1, r+dx[i], c+dy[i])

# Write the answer to the output file.
for r in xrange(num_rows):
    for c in xrange(num_cols):
        outputFile.write(str(grid[num_days%2][r][c]))
    outputFile.write("\n")

# Finally, close the input/output files.
inputFile.close()
outputFile.close()
