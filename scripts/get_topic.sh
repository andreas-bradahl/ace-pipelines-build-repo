#!/bin/bash

set -eu

TOKEN=$1
GH_USER=$2
REPO=$3

echo $(curl \
    -s \
    -u tip-github:"$TOKEN" \
    -H "Accept: application/vnd.github.v3+json" \
    https://api.github.com/repos/${GH_USER}/${REPO} | 
    jq -r '.topics[] | select(. | startswith("project"))')