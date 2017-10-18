# Prints the pymol commands for selecting all clusters in the given clusters file and number of clusters.
# First argument is the file name, second argument is the number of clusters.
pre1="select clust"
pre2=", resi "
END="$2"
for ((i=0;i<END;i++)); do
    awk -v clust=$i 'BEGIN {printf "select clust%d, resi ", clust} {if($2 == clust){printf "%d+", $1+1;}}' "$1"
    # Print newline
    echo ""
done
