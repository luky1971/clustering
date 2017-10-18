# Utility functions used by clustering scripts.
import csv
import sys


def csv_to_matrix(csvfilename):
    """
    Reads the file at the given path and returns a float matrix,
    or None if there was an error.
    """
    try:
        with open(csvfilename) as csvfile:
            ret = []
            csvreader = csv.reader(csvfile, delimiter=',')
            for row in csvreader:
                ret.append([float(x) for x in row])
            return ret
    except IOError:
        print('Failed to read', csvfilename, file=sys.stderr)
    return None


def replace_inf(mat):
    """
    Replaces all infinite values in mat with a very high floating point number,
    returning the resulting matrix (without modifying mat).
    """
    if mat is None:
        return None
    high = sys.float_info.max
    ret = []
    for row in mat:
        ret.append([x if x <= high else high for x in row])
    return ret


def print_list(in_list, file=sys.stdout):
    """
    Prints the given list as rows of index value
    """
    for index, elem in enumerate(in_list):
        print(index, elem, file=file)