#!/bin/bash

unset DISPLAY
numexamples=$(find *.py -type f | wc -l)
index=1
for filename in *.py; do
    echo Running example $index/$numexamples: "$filename"
    python3 $filename > /dev/null
	index=$((index+1))
done

rm -rf *.png *.csv *.h5
