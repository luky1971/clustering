# Finds the neighbors of each row in a csv matrix based on
# a distance cutoff, and generates a cumulative distribution
# of number of neighbors.
# Arg 1: input file name
# Arg 2: the distance cutoff below (or equal to) which
# two elements are considered neighbors
import sys
from util import csv_to_matrix, replace_inf, cum_dist, print_sorted_dict

if len(sys.argv) < 3:
    print('csv input file name and distance cutoff must be provided!')
    sys.exit(1)

cutoff = float(sys.argv[2])
mat = csv_to_matrix(sys.argv[1])

if mat is not None:
    mat = replace_inf(mat)
    neighbor_counts = []

    # count neighbors
    for row in mat:
        neighbors = 0
        for x in row:
            if x <= cutoff:
                neighbors += 1
        neighbor_counts.append(neighbors)

    # generate cumulative distribution
    dist = cum_dist(neighbor_counts)

    # print the distribution
    print_sorted_dict(dist)
else:
    print('Error loading csv', sys.argv[1], 'as matrix')