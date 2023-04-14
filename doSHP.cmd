#!/bin/bash
files=/Users/emilzegers/testdata/gelderland-latest-free.shp/*.shp
for shp in $files;
do
    ls $shp
    ogr2ogr -f GeoJSONSeq $shp.json $shp
done
