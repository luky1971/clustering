# Prints the residue IDs of the selected cluster for selection in PyMol
awk -v clust="$2" '{if($2 == clust){printf "%d+", $1+1;}}' "$1"
# Print newline
echo ""
