'''
Task1: Find the length of a given DNA sequence in FASTA format.
Date : 16/11/2022
Author: Dinuri Vishara Lokuwalpola
'''

#Read the FASTA file with DNA sequence and assign it to a variable “file1”.
file1= open("Q1_4.txt",'r')

#Declare a variable “count” and initialize it to zero.
count = 0

#Use a for loop to read the FASTA file line by line.
#Remove escape characters in lines.
#Remove the heading of the FASTA file.
for line in file1:
    lines= line.strip()
    if lines != '\n':
        if '>' not in lines:
            print(lines)

            #Use another for loop to read each character in a line.
            #Increment the “count” variable by one in each iteration.
            for base in lines:
                count+=1

#Return “count”.
print("Length of the DNA sequence: " , count)

#close the file.
file1.close()






