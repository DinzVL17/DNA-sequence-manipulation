'''
Task2: Find the length of a given DNA sequence in FASTA format
using len() function in python.
Date : 16/11/2022
Author: Dinuri Vishara Lokuwalpola
'''

# Read the FASTA file with DNA sequence.
file2= open("Q1_4.txt",'r')

# Declare a variable “count” and initialize it to zero.
count =0

# Use a for loop to read the FASTA file line by line.
for line in file2:
    # Remove escape characters in lines.
    lines = line.strip()
    if lines != '\n':
        #step5: remove the heading of the FASTA file
        if '>' not in lines:
            #Step6: get the length of a line and sum it up
            count  = count + len(lines)

# return the count
print("Length of the DNA sequence: ", count)

# close the file
file2.close()

























