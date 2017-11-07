#!/bin/bash
# Counts the number of clusters in a clustering output file.
# The only argument is the output file name.
cut -f2 -d' ' $1 | sort | uniq | wc -l
