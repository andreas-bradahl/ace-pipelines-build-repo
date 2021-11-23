#!/bin/bash
# Start this script from the root folder of the application.
#
# Moves all project subfolders that are located 
# inside the 'projects' folder of an 
# application to a common workspace.

WORKSPACE_DIR="projects_workspace"
PROJECTS_DIR="projects"

# Create workspace directory
if [[ ! -d "$WORKSPACE_DIR" ]];
then
    mkdir -p $WORKSPACE_DIR
fi

for dir in */
do
    echo $dir
done

# Copy all directories in 'projects' folder to workspace
# if [[ -d "$PROJECTS_DIR" ]];
# then
#     cp -r $PROJECTS_DIR/* $WORKSPACE_DIR
# else
#     echo "No '$PROJECTS_DIR' folder found."
# fi
