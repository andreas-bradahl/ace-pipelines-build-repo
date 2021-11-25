#!/bin/bash

for dir in $1/*/;
do
    if [[ ${dir^^} == *"LIB/" || ${dir^^} == *"JAVA/" || $(basename ${dir^^}) == "TIP000"* ]]; then
        continue
    else
        echo $(basename "$dir")
    fi
done