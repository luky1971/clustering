# Prints the residue IDs of the selected cluster for selection in PyMol.
# First argument is the file name, second argument is the cluster number.
awk -v clust="$2" '{if($2 == clust){printf "%d+", $1+1;}}' "$1"
# Print newline
echo ""
