# Performs affinity propagation clustering on an input affinity matrix.
# Arg 1: input file name
# Arg 2: damping
# Arg 3: max number of iterations
# Arg 4: (optional) flag '-centers' if you want to print the indexes of the cluster centers
import sys
from sklearn.cluster import AffinityPropagation
from util import csv_to_matrix, replace_inf, print_list

if len(sys.argv) < 2:
    print('csv input file name must be provided!')
    sys.exit(1)

infile = sys.argv[1]
damping = 0.5
max_iter = 200

if len(sys.argv) > 2:
    damping = float(sys.argv[2])

if len(sys.argv) > 3:
    max_iter = int(sys.argv[3])

show_centers = False
if len(sys.argv) > 4:
    show_centers = sys.argv[4] == '-centers'

x = replace_inf(csv_to_matrix(infile))

if x is not None:
    affprop = AffinityPropagation(damping=damping, max_iter=max_iter, affinity='precomputed')
    y = affprop.fit_predict(x)
    if show_centers:
        for ind in affprop.cluster_centers_indices_:
            print(ind)
    else:
        print_list(y)
