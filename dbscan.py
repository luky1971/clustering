# Performs DBSCAN clustering on an input distance matrix.
# Arg 1: input file name
# Arg 2: value for DBSCAN's epsilon parameter
# Arg 3: value for DBSCAN's min_samples parameter
import sys
from sklearn.cluster import DBSCAN
from util import csv_to_matrix, replace_inf, print_list

if len(sys.argv) < 2:
    print('csv input file name must be provided!')
    sys.exit(1)

infile = sys.argv[1]
eps = 10
min_samples = 3

if len(sys.argv) > 2:
    eps = float(sys.argv[2])

if len(sys.argv) > 3:
    min_samples = int(sys.argv[3])

# load the distance matrix
x = replace_inf(csv_to_matrix(infile))

if x is not None:
    # cluster
    y = DBSCAN(eps=eps, min_samples=min_samples, metric='precomputed').fit_predict(x)
    # print cluster labels
    print_list(y)