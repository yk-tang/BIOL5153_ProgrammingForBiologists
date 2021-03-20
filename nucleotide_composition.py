#! /usr/bin/env python3

# set the name of input DNA sequence file
filename = 'dna.txt'

# # open the input file, assign to file handle called 'infile'
infile = open(filename, 'r')

# read the file
dna_sequence = infile.read().rstrip()

# print the dna sequence
# print(dna_sequence)

# close the file
infile.close()

# print the sequence
# print(dna_sequence)

# Calculate sequence length
seqlen = len(dna_sequence)
print('sequence length:', seqlen)

# frequency of A
numA = dna_sequence.count('A')
A = numA/seqlen 
freqA = round(A, 3)
print('Freq of A:', freqA)

# frequency of C
numC = dna_sequence.count('C')
C = numC/seqlen 
freqC = round(C, 3)
print('Freq of C:', freqC)

# frequency of G
numG = dna_sequence.count('G')
G = numG/seqlen 
freqG = round(G, 3)
print('Freq of G:', freqG)

# frequency of T
numT = dna_sequence.count('T')
T = numT/seqlen 
freqT = round(T, 3)
print('Freq of T:', freqT)

# G + C content
sumGC = G + C
GC = round(sumGC, 3)
print('G+C content:', GC)

# Frequency sum check script
# FreqCheck = A + C + G + T
# print('Sum of frequencies:', FreqCheck)