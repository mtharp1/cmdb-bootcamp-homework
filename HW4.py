#!/usr/bin/env python

#/Users/cmdb/cmdb-bootcamp-homework/SRR072893_thout $ awk '$3=="transcript"' transcripts.gtf | grep "+" > plus_transcripts.txt

#/Users/cmdb/cmdb-bootcamp-homework/SRR072893_thout $ awk '$3=="transcript"' transcripts.gtf | grep "-" > minus_transcripts.txt

#/Users/cmdb/cmdb-bootcamp-homework/SRR072893_thout $ bedtools flank -l 250 -r 0 -i plus_transcripts.gtf -g /Users/cmdb/cmdb-bootcamp-homework/genome_columns.gff > plus_transcripts_250.gtf

#/Users/cmdb/cmdb-bootcamp-homework/SRR072893_thout $ bedtools slop -l 0 -r 250 -i plus_transcripts_250.gtf -g /Users/cmdb/cmdb-bootcamp-homework/genome_columns.gff > plus_transcripts_slop_500.gtf 

#/Users/cmdb/cmdb-bootcamp-homework/SRR072893_thout $ bedtools getfasta -fi /Users/cmdb/data/genomes/dmel-all-chromosome-r5.57.fasta -bed plus_transcripts_500.gtf -fo plus_seq_500.fasta

#/Users/cmdb/cmdb-bootcamp-homework/SRR072893_thout $ bedtools flank -l 0 -r 250 -i minus_transcripts.gtf -g /Users/cmdb/cmdb-bootcamp-homework/genome_columns.gff > minus_transcripts_250_2.gtf

#/Users/cmdb/cmdb-bootcamp-homework/SRR072893_thout $ bedtools slop -l 250 -r 0 -i minus_transcripts_250_2.gtf -g /Users/cmdb/cmdb-bootcamp-homework/genome_columns.gff > minus_transcripts_500_2.gtf

#/Users/cmdb/cmdb-bootcamp-homework/SRR072893_thout $ bedtools getfasta -s -fi /Users/cmdb/data/genomes/dmel-all-chromosome-r5.57.fasta -bed minus_transcripts_500_2.gtf -fo minus_seq_500.fasta


#Use to find GC content
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

        if line.startswith (">") == gene_name: 
        
        "G" or nucleotides [i] == "C"):
            GC_counter += 1
            #=GC_counter + 1
        elif (nucleotides [i] == "A" or nucleotides [i] == "T"):
            AT_counter += 1
        else:
            break

fraction_GC = GC_counter / (GC_counter + AT_counter)

print fraction_GC


#Use to make linear regression model
#!/usr/bin/env python
import pandas
import matplotlib.pyplot as plot
import statsmodels.api as sm

df = pandas.read_csv( "GC_content.csv", index_col=0)
model = sm.formula.ols( formula="gene_name~fraction_GC", data=df )
#left of ~ dependent variable, right of ~ is independent variable
res = model.fit()
print res.summary()

plot.scatter( df["gene_name"], df["fraction_GC"] )
plot.savefig( "GC_content.png" )



