#!/bin/bash

TOKEN=$1
GH_USER=$2
TOPIC=$3
OUTFILE=$4

curl \
    -s \
    -u tip-github:"$TOKEN" \
    -H "Accept: application/vnd.github.v3+json" \
    "https://api.github.com/search/repositories?q=user:${GH_USER}+topic:${TOPIC}" | 
    jq -r '[.items[].name]' > $OUTFILE