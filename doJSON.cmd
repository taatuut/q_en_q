#!/bin/bash
for i in {1..2};
do
    echo
    echo Begin $i
    echo
    jq -c '.products.product[] | select(."@id"=="'$i'")' data/output/product_descriptions_*.json >> data/output/products/productid_$i.json
    echo
    echo End $i
    echo
done