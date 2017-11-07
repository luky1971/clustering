# Generates a cumulative distribution for the values in an input csv,
# after rounding each value to its nearest int.
# Arg 1: input file name
import sys
from util import csv_to_matrix, replace_inf, cum_dist, print_sorted_dict

if len(sys.argv) < 2:
    print('csv input file name must be provided!')
    sys.exit(1)

mat = csv_to_matrix(sys.argv[1])
# flattened values from matrix mat
vals = []

if mat is not None:
    mat = replace_inf(mat)

    # flatten the matrix
    for row in mat:
        vals += row

    # build the cumulative distribution
    dist = cum_dist(vals)

    # print the cumulative distribution
    print_sorted_dict(dist)
else:
    print('Error loading csv', sys.argv[1], 'as matrix')