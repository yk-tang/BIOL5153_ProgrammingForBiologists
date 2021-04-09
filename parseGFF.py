#! /usr/bin/env python3

import csv
import argparse
from Bio import SeqIO

# inputs: 1) GFF file, 2) corresponding genome sequence (FASTA format)

# create an argument parser object
parser = argparse.ArgumentParser(description='This script will parse a GFF file and extract each feature from the genome')

# add positional arguments
parser.add_argument("gff", help='name of the GFF file')
parser.add_argument("fasta", help='name of the FASTA file')

# parse the arguments
args = parser.parse_args()

# read in FASTA file
genome = SeqIO.read(args.fasta, 'fasta')
print(genome.id)
#print(genome.seq)

# open and read in GFF file
with open(args.gff, 'r') as gff_in:

    # create a csv reader object
    reader = csv.reader(gff_in, delimiter='\t')

    # loop over all the lines in our reader objects (i.e., parsed file)
    for line in reader:
        start   = int(line[3]) - 1
        end     = int(line[4]) + 1
        feature = line[8]
        print(feature)

        # extract the sequence
        print(genome.seq[start:end])

