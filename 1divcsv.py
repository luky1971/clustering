# This script reads a csv file, divides 1 by each element, and outputs the result.
import csv
import math
import sys

if len(sys.argv) < 3:
    print('csv input and output file names, respectively, must be provided!')
    sys.exit(1)

infile = sys.argv[1]
outfile = sys.argv[2]

try:
    with open(infile) as csvin:
        csvreader = csv.reader(csvin, delimiter=',')

        try:
            with open(outfile, 'w') as csvout:
                csvwriter = csv.writer(csvout, delimiter=',')
                for row in csvreader:
                    csvwriter.writerow([(1/float(x)) if float(x) > sys.float_info.epsilon else math.inf for x in row])
        except IOError:
            print('Failed to open file for writing:', outfile, file=sys.stderr)
except IOError:
    print('Failed to read', infile, file=sys.stderr)
