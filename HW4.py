#!/usr/bin/env python

import sys

list_gene_names = []
list_fraction_GC = []

while 1:
    line = sys.stdin.readline()
    if line.startswith (">"):
        list_gene_names = line
        list_gene_names.append( list_gene_names )
    elif line == "":
        break
    else:
        
GC_counter = 0.0
AT_counter = 0.0

    if line.startswith (">") == gene_name 
        
        "G" or nucleotides [i] == "C"):
            GC_counter += 1
            #=GC_counter + 1
        elif (nucleotides [i] == "A" or nucleotides [i] == "T"):
            AT_counter += 1
        else:
            break

fraction_GC = GC_counter / (GC_counter + AT_counter)

print fraction_GC





