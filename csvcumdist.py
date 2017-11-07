# Generates a cumulative distribution for the values in an input csv,
# after rounding each value to its nearest int.
# Arg 1: input file name
import sys
from util import csv_to_matrix, replace_inf

if len(sys.argv) < 2:
    print('csv input file name must be provided!')
    sys.exit(1)

mat = csv_to_matrix(sys.argv[1])
# flattened values from matrix mat
vals = []
# mapping from matrix value -> sum of instances <= value
cumdist = {}

if mat is not None:
    mat = replace_inf(mat)

    # flatten and sort the matrix
    for row in mat:
        vals += row
    vals.sort()

    # build the cumulative distribution
    n = len(vals)
    for i in range(n):
        cumdist[int(vals[i])] = (i+1) / n

    # print the cumulative distribution
    for key in sorted(cumdist.keys()):
        print(key, cumdist[key])
else:
    print('Error loading csv', sys.argv[1], 'as matrix')