#!/bin/sh
# Description:
# Retrieves a GitHub topic that represents the pod which the application
# belongs to. If it doesn't belong to a specific pod yet, null is
# returned.
#
# Arguments:
# $1: GitHub user/organization in which the repository resides
# $2: GitHub repository to search for topic in
#
# @author: Andreas Bradahl <andreas.bradahl@tine.no>

# apk add jq curl > /dev/null

curl \
    -H "Accept: application/vnd.github.v3+json" \
    https://api.github.com/repos/$1/$2 # | jq -r '.topics[] | select(. | startswith("pod"))'