#!/bin/bash
# Start this script from the workspace where all application
# folders are placed. Application folders contain config, 
# projects etc.
#
# Moves all project subfolders that are located 
# inside the 'projects' folder of an 
# application to a common workspace.

ALL_PROJECTS_WORKSPACE=$1
PROJECTS_FOLDER=$2

# Create workspace directory
if [[ ! -d "$ALL_PROJECTS_WORKSPACE" ]]; then
    mkdir -p $ALL_PROJECTS_WORKSPACE
fi

for dir in */; do
    # Copy all directories in 'projects' folder to workspace
    if [[ -d $dir/"$PROJECTS_FOLDER" ]]; then
        echo "Copying all project folders from $dir to $ALL_PROJECTS_WORKSPACE"
        cp -r $dir/$PROJECTS_FOLDER/* $ALL_PROJECTS_WORKSPACE
    else
        echo "No '$PROJECTS_FOLDER' folder found for application $dir."
    fi
done
