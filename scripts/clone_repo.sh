#!/bin/bash
ORG=$1
REPO=$2
BRANCH=$3
CLONE_DESTINATION=$4

clone_repo() {
    local url="https://github.com/${ORG}/${REPO}.git"

    git clone -b $BRANCH $url common-workspace/$REPO
}

clone_repo