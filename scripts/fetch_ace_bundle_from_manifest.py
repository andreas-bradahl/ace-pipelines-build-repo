import os
import sys

import yaml

manifest_file = sys.argv[1]
branch = sys.argv[2]
repos_working_dir = sys.argv[3]

def clone_app(repo, branch, repos_working_dir):
    url = f'https://github.com/tineikt/{repo}.git'
    clone = f'git clone -b {branch} {url} {repos_working_dir}/{repo}'
    if not os.path.exists(f'{repos_working_dir}/{repo}'):
        os.system(clone)
    else:
        print(f'Dependency {repo} already fetched.')

with open(manifest_file, 'r') as f:
    manifest_object = yaml.safe_load(f)

for app in manifest_object['applications']:
    clone_app(app, branch, repos_working_dir)

for dep in manifest_object['dependencies']:
    clone_app(dep, branch, repos_working_dir)