#!/bin/bash
for for i in {0..10..1};
do
    echo.
    echo $i
    echo.
    jq -c '.products.product[] | select(."@id"=="$i")' data/output/product_descriptions_*.json >> data/output/products/$i.json
done