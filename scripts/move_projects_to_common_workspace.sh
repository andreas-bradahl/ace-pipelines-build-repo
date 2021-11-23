#!/bin/bash
# Start this script from the workspace where all application
# folders are placed.
#
# Moves all project subfolders that are located 
# inside the 'projects' folder of an 
# application to a common workspace.

WORKSPACE_DIR="../projects_workspace"
PROJECTS_DIR="projects"

# Create workspace directory
if [[ ! -d "$WORKSPACE_DIR" ]]; then
    mkdir -p $WORKSPACE_DIR
fi

for dir in */
do
    # Copy all directories in 'projects' folder to workspace
    if [[ -d $dir/"$PROJECTS_DIR" ]]; then
        echo "Putting $dir projects in projects_workspace"
        cp -r $dir/$PROJECTS_DIR/* $WORKSPACE_DIR
    else
        echo "No '$PROJECTS_DIR' folder found for application $dir."
    fi
done
