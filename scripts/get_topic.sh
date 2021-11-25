#!/bin/bash

TOKEN=$1
USER=$2
REPO=$3

echo $(curl \
    -s \
    -u tip-github:"$TOKEN" \
    -H "Accept: application/vnd.github.v3+json" \
    https://api.github.com/repos/${USER}/${REPO} | 
    jq -r '.topics[] | select(. | startswith("pod"))')