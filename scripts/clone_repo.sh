#!/bin/bash
ORG=$1
REPO=$2
BRANCH=$3

clone_repo() {
    local url="https://github.com/${ORG}/${REPO}.git"

    echo $ORG
    echo $REPO
    echo $BRANCH
    echo $url

    git clone -b $BRANCH $url common-workspace/$REPO
}

clone_repo