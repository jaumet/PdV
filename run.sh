#!/bin/sh

if [ "$1" = "" ] ; then
        echo
        echo "Usage: sh run.sh [export | grouping | relocate]"
        echo
fi

if [ "$1" = "export" ] ; then
    echo "Liberating xlsx files..."
    python xlsx2tsv.py data/key.xlsx > data-tmp/key.tsv
    python xlsx2tsv.py data/feedback.xlsx > data-tmp/feedback.tsv

    echo "Combining 2 TSV files into XML"
    python tsv2xml.py > data-tmp/votations.xml
fi

if [ "$1" = "grouping" ] ; then
    echo "grouping dummy..."
fi

if [ "$1" = "relocate" ] ; then
    echo "Data analysis + relocation + output"
    python analyzer.py
fi

echo "bye :-)"




