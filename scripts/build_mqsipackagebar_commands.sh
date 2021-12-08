#!/bin/bash

REPO_LIST=$1
PROJECTS_WORKSPACE=$2
OUTFILE=$3

set -eu

jq -cr '.[]' "$REPO_LIST" | while read repo; do
    TIP_NUMBER=${repo:3:3}
    # TIP_NUMBER=${TIP_NUMBER^^}
    PACKAGE_COMMAND="mqsipackagebar -a ../bars/${repo}.bar -k"
    # EXCLUDE_PATTERN='\b[tT][iI][pP]000[A-Za-z0-9-_]+|[tT][iI][pP]\d{3}[A-Za-z0-9-_]+[lL][iI][bB]|Java\b'

    for dir in "$PROJECTS_WORKSPACE"/*/; do
        echo "Currently handling: $(basename $dir)"
    # for dir in "$PROJECTS_WORKSPACE"/[tT][iI][pP]${TIP_NUMBER}*/; do
        # if [[ $(basename "$dir") =~ $EXCLUDE_PATTERN ]]; then
        if [[ ${dir^^} == *"LIB/" || ${dir^^} == *"JAVA/" || $(basename "${dir^^}") == "TIP000"* ]]; then
            continue
        elif [[ $(basename "$dir") =~ [tT][iI][pP]${TIP_NUMBER}* ]]; then
            PACKAGE_COMMAND+=" "$(basename "$dir")
        else
            echo "No valid application folder found - exiting..."
            exit 1
        fi
    done
    echo "$PACKAGE_COMMAND" | tee -a "$OUTFILE"
done