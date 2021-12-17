#!/bin/bash

REPO_LIST=$1
PROJECTS_WORKSPACE=$2
OUTFILE=$3

set -eu

jq -cr '.[]' "$REPO_LIST" | while read repo; do
    TIP_NUMBER=${repo:3:3}
    echo "Creating mqsipackagebar command for TIP$TIP_NUMBER"
    PACKAGE_COMMAND="mqsipackagebar -a ../bars/${repo}.bar -k"
    # EXCLUDE_PATTERN='\b[tT][iI][pP]000[A-Za-z0-9-_]+|[tT][iI][pP]\d{3}[A-Za-z0-9-_]+[lL][iI][bB]|Java\b'

    for dir in "$PROJECTS_WORKSPACE"/*/; do
        echo "Checking folder $(basename $dir)"
        # if [[ $(basename "$dir") =~ $EXCLUDE_PATTERN ]]; then
        if [[ $(basename "${dir^^}") == *"LIB" || $(basename "${dir^^}") == *"JAVA" || $(basename "${dir^^}") == "TIP000"* ]]; then
            echo "Folder $(basename $dir) matched pattern LIB, Java or TIP000 - skipping"
            continue
        elif [[ $(basename "$dir") =~ [tT][iI][pP]${TIP_NUMBER}* ]]; then
            echo "Adding folder $(basename "$dir") to mqsipackagebar command"
            PACKAGE_COMMAND+=" "$(basename "$dir")
        else
            echo "No pattern matched for folder $(basename "$dir")"
        fi
    done
    echo "$PACKAGE_COMMAND" | tee -a "$OUTFILE"
done