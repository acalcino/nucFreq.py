#!/usr/bin/env python

import sys

# check if a filename was provided as a command line argument
if len(sys.argv) < 2:
    print("Error: no input file provided.")
    print("Usage: python script.py input.fasta")
    sys.exit(1)

# get the input filename from the command line argument
input_filename = sys.argv[1]

# open the input file and read the lines
try:
    with open(input_filename) as f:
        lines = f.readlines()
except IOError:
    print("Error: unable to read input file '{}'".format(input_filename))
    sys.exit(1)

# check if the input file is in the correct format (FASTA)
if not all(map(lambda x: x.startswith('>') or x.startswith('A') or x.startswith('T') or x.startswith('C') or x.startswith('G') or x.startswith('a') or x.startswith('t') or x.startswith('c') or x.startswith('g'), lines)):
    print("Error: input file is not in FASTA format.")
    print("Expected lines starting with '>' or 'A', 'T', 'C', or 'G'")
    sys.exit(1)

# initialize counters for each nucleotide and position
max_pos = 0
counts = {'A': [], 'T': [], 'C': [], 'G': []}

# iterate over the sequences in the file
for line in lines:
    # skip lines that are not sequences
    if not line.startswith('>'):
        # get the number of positions in the sequence
        num_pos = len(line.strip())
        # update the maximum number of positions
        max_pos = max(max_pos, num_pos)
        # initialize the counts for each position in the sequence
        for i in range(num_pos):
            counts['A'].append(0)
            counts['T'].append(0)
            counts['C'].append(0)
            counts['G'].append(0)

# iterate over the sequences in the file
for line in lines:
    # skip lines that are not sequences
    if not line.startswith('>'):
        # iterate over the characters in the sequence
        for i, c in enumerate(line.strip()):
            # increment the count for the current nucleotide and position
            counts[c.upper()][i] += 1

 # print the header line
print("\t", end="")
for i in range(max_pos):
    print("Position {}\t".format(i + 1), end="")
print()

# print the counts for each nucleotide
for nuc in ["A", "T", "C", "G"]:
    print(nuc + "\t", end="")
    for i in range(max_pos):
        print("{}\t".format(counts[nuc][i]), end="")
    print()
