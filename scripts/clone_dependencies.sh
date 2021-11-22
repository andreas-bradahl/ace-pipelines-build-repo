#!/bin/bash
ORG=$1
DEP=$2

clone_dependency() {
    local url="https://github.com/${ORG}/${DEP}.git"

    echo $ORG
    echo $DEP
    echo $url

    git clone -b master $url common-workspace/$DEP
}

clone_dependency