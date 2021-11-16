#!/bin/bash

for dir in common-workspace/*;
do
    if [[ $dir == *"Library" || $dir == *"Java" ]];
    then
        continue
    else
        echo "$dir"
    fi
done