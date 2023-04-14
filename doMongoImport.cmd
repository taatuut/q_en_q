#!/bin/bash
files=/Users/emilzegers/testdata/gelderland-latest-free.shp/json/import/*.json
for json in $files;
do
    #ls $json
    file="${json##*/}"
    file="${file%.*.*}"
    echo $file
    # mongodb_uri must be available as environment variable
    mongoimport --uri=$mongodb_uri --collection=$file --drop --file=$json
done
