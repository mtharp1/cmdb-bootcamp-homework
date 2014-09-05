#!/usr/bin/env python

import sys

from fasta import FASTAReader

reader = FASTAReader( sys.stdin )

seq_length = []
actual_sequences = []
list_of_doubles = []

for sid, sequence in reader:
    seq_length.append(len(str(sequence)))
    actual_sequences.append(str(sequence))
    list_of_doubles = zip(seq_length, actual_sequences) #zip makes duple
   
    print list_of_doubles
   
    
sort_list = sorted(list_of_doubles[0], reverse=True)

transcripts = sort_list[0:100]


