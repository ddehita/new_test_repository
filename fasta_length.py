#!env python

"""#Aniade un comentario al script
Python script to count the number of aminoacidsor nucleotides per sequence in a FASTA file
Call it like so:
    python fasta_length.py sequences.fasta
"""

import sys

sequence_length = 0 #an integer
fasta_sequence_lengths = []

# Getting the filename from the list of arguments
fasta_filename = sys.argv[1] #llama a la secuencia fasta

# Opening the file:
fastafile = open(fasta_filename, 'r') #Abre el archivo solo para leerlo 'r'

# Iterating over all lines in the file:
for line in fastafile.readlines():
    if line.startswith('>'):
        if sequence_length:
            fasta_sequence_lengths.append(sequence_length)
        sequence_length = 0
    else:
        sequence_length += len(line.strip()) #+= es un shortcut que significa sequence_length + len(line.strip())
fasta_sequence_lengths.append(sequence_length)

# Closing the file:
fastafile.close() #Siempre se necesita cerrar el archivo despues de abrirlo con open

print(sorted(fasta_sequence_lengths))
