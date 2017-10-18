# Performs agglomerative hierarchical clustering on an input matrix.
# Arg 1: input file name
# Arg 2: number of clusters
# Arg 3: linkage method to use in agglomerative clustering (ward, complete, or average)
import sys
from sklearn.cluster import AgglomerativeClustering
from util import csv_to_matrix, replace_inf, print_list

if len(sys.argv) < 2:
    print('csv input file name must be provided!')
    sys.exit(1)

infile = sys.argv[1]
nclusters = 2
linkage = 'complete'

if len(sys.argv) > 2:
    nclusters = int(sys.argv[2])

if len(sys.argv) > 3:
    linkage = sys.argv[3]

x = replace_inf(csv_to_matrix(infile))

if x is not None:
    y = AgglomerativeClustering(n_clusters=nclusters, affinity='precomputed', linkage=linkage).fit_predict(x)
    print_list(y)