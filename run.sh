#!/bin/sh

echo "Liberating xlsx files..."
python xlsx2tsv.py data/key.xlsx > data-tmp/key.tsv
python xlsx2tsv.py data/feedback.xlsx > data-tmp/feedback.tsv

echo "Combining 2 TSV files into XML"
python tsv2xml.py > data-tmp/votations.xml

echo "Data analysis + relocation + output"
python analyzer.py

