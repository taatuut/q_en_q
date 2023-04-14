#!/bin/bash
for pd in data/product_descriptions_*.xml;
do
    #ls $pd
    file="${pd##*/}"
    file="${file%.*}"
    echo $file
    cat $pd | xq > data/output/$file.json
done