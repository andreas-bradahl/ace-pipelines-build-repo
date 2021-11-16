#!/bin/bash
# Start this script from the root folder of the application.
#
# Moves all files that are located inside the 'projects' folder of an 
# application to a common workspace.

WORKSPACE_DIR="../common-workspace"

if [[ ! -d "$WORKSPACE_DIR" ]];
then
    mkdir $WORKSPACE_DIR
fi

PROJECTS_DIR="projects"

if [[ -d "$PROJECTS_DIR" ]];
then
    cp -r $PROJECTS_DIR/* $WORKSPACE_DIR
else
    echo "No '$PROJECTS_DIR' folder found."
fi