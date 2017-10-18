# Performs affinity propagation clustering on an input affinity matrix.
# Arg 1: input file name
# Arg 2: number of clusters
# Arg 3: strategy used to assign embedding space labels, ‘kmeans’ or ‘discretize’
import sys
from sklearn.cluster import SpectralClustering
from util import csv_to_matrix, replace_inf, print_list

if len(sys.argv) < 2:
    print('csv input file name must be provided!')
    sys.exit(1)

infile = sys.argv[1]
n_clusters = 8
assign_labels = 'kmeans'

if len(sys.argv) > 2:
    n_clusters = int(sys.argv[2])

if len(sys.argv) > 3:
    assign_labels = sys.argv[3]

x = replace_inf(csv_to_matrix(infile))

if x is not None:
    y = SpectralClustering(n_clusters=n_clusters, affinity='precomputed', assign_labels=assign_labels).fit_predict(x)
    print_list(y)