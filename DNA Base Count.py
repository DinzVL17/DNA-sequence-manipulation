'''
Task3: calculation of the nucleotide base counts of a given DNA sequence in FASTA format
Date : 16/11/2022
Author: Dinuri Vishara Lokuwalpola
'''

adenine=0
guanine=0
cytosine=0
thymine=0
file1= open("Q1_4.txt", 'r')
for line in file1:
    lines=line.strip()
    if lines != '\n':
        if '>' not in lines:
            for base in lines:
                if (base=='A'):
                    adenine+=1
                elif(base=='G'):
                    guanine+=1
                elif(base=='C'):
                    cytosine+=1
                elif(base=='T'):
                    thymine+=1
print("Adenine count is: ", adenine, "\n"
    "Guanine count is: ", guanine, "\n"
    "Cytosine count is: ", cytosine, "\n"
    "Thymine count is: ", thymine)