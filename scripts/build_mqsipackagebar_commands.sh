#!/bin/bash

REPO_LIST=$1
PROJECTS_WORKSPACE=$2
OUTFILE=$3

set -eu

jq -cr '.[]' "$REPO_LIST" | while read repo; do
    TIP_NUMBER=${repo:3:3}
    # TIP_NUMBER=${TIP_NUMBER^^}
    PACKAGE_COMMAND="mqsipackagebar -a ../bars/${repo}.bar -k"

    for dir in "$PROJECTS_WORKSPACE"/[tT][iI][pP]${TIP_NUMBER}*/; do
        if [[ ${dir^^} == *"LIB/" || ${dir^^} == *"JAVA/" || $(basename "${dir^^}") == "TIP000"* ]]; then
            continue
        else
            PACKAGE_COMMAND+=" "$(basename "$dir")
        fi
    done
    echo "$PACKAGE_COMMAND" | tee -a "$OUTFILE"
done