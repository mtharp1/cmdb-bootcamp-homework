#!/bin/bash

#
# Day 1 - Homework: Part 2 - debug this bash script
#

echo "There are around 6 mistakes"

FASTQ_DIR="/Users/cmdb/data/fastq"
OUTPUT_DIR="/Users/cmdb/data/day1"

GENOME_DIR="/Users/cmdb/data/genomes"
SAMPLE_PREFIX="SRR072"

ANNOTATION=dmel-all-r5.57.gff

CORES=$(seq24)

for i in $FASTQ_DIR $OUTPUT_DIR $GENOME_DIR $SAMPLE_PREFIX
do
  echo fastqc $FASTQ_DIR/$SAMPLE_PREFIX$i\.fastq.gz -o $OUTPUT_DIR
  echo tophat $FASTQ_DIR/$SAMPLE_PREFIX$i\.fastq.gz -o $OUTPUT_DIR
  echo cufflinks $FASTQ_DIR/$SAMPLE_PREFIX$i\.fastq.gz -o $OUTPUT_DIR
done
  
  