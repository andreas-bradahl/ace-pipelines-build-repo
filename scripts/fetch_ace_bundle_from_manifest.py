"""Fetch ACE bundle from manifest

This script reads a manifest.yaml file with information about an IBM 
ACE bundle (of applications and dependencies). It reads the
'applications' and 'dependencies' array sections, and clones
each of them to a common workspace directory.

Script requires that moduel 'pyyaml' is installed.
"""

import os
import sys
import json

import yaml

def clone_app(repo, branch, repos_working_dir):
    url = f'https://github.com/tineikt/{repo}.git'
    clone = f'git clone -b {branch} {url} {repos_working_dir}/{repo}'
    if not os.path.exists(f'{repos_working_dir}/{repo}'):
        os.system(clone)
    else:
        print(f'Dependency {repo} already fetched.')

manifest_file = sys.argv[1]
branch = sys.argv[2]
repos_working_dir = sys.argv[3]
repo_list_file = sys.argv[4]

# Script execution code
def main():
    try:
        with open(manifest_file, 'r') as f:
            manifest_object = yaml.safe_load(f)
    except OSError as e:
        print("Error reading manifest file")
        sys.exit(1)

    repo_list = []
    for app in manifest_object['applications']:
        clone_app(app, branch, repos_working_dir)
        repo_list.append(app)

    # Create repo list file
    with open(repo_list_file, 'w') as r:
        json.dump(repo_list, r)

    for dep in manifest_object['dependencies']:
        clone_app(dep, branch, repos_working_dir)

main()