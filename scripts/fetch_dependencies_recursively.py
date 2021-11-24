import sys
import os
import json

def fetch_deps_recursive(repo, working_dir):
    url = f'https://github.com/tineikt/{repo}.git'
    workspace = 'common-workspace'

    os.chdir(working_dir)

    clone = f'git clone -b cicd {url} {workspace}/{repo}'
    if not os.path.exists(f'{workspace}/{repo}'):
        os.system(clone)
        os.chdir(f'{workspace}/{repo}')
        
        try:
            with open('dependencies.json', 'r') as deps_file:
                data = deps_file.read()
            
            dependencies = json.loads(data)
            for dep in dependencies:
                if dep:   
                    fetch_deps_recursive(dep, working_dir)
        except IOError:
            print(f'No dependencies file for {repo}.')
    else:
        print(f'Dependency {repo} already fetched.')
        
def main():
    repo = sys.argv[1]
    working_dir = sys.argv[2]

    fetch_deps_recursive(repo, working_dir)

if __name__ == "__main__":
    main()