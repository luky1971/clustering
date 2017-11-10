# Reads a csv matrix and sets the value between each element and itself,
# and its adjacent neighbors, to 0.
# Assumes that the matrix is square.
# Arg 1: input filename
# Arg 2: output filename
# Arg 3: number of neighbors on each side to set to 0
import csv
import sys
from util import csv_to_matrix

if len(sys.argv) < 4:
    print('Input filename, output filename, and number of neighbors required!')
    sys.exit(1)

infile = sys.argv[1]
outfile = sys.argv[2]
num_neighbors = int(sys.argv[3])

mat = csv_to_matrix(infile)

if mat is not None and len(mat) > 0:
    maxind = len(mat) - 1
    # turn off neighbors
    for i in range(0, len(mat)):
        for offset in range(0, num_neighbors+1):
            left = max(0, i - offset)
            right = min(i + offset, maxind)
            mat[i][left] = 0
            mat[i][right] = 0
    # print modified matrix as new csv
    with open(outfile, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(mat)
