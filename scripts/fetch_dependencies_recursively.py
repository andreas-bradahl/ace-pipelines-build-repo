import sys
import os
import json

def fetch_deps_recursive(repo):
    url = f'https://github.com/tineikt/{repo}.git'
    workspace = 'common-workspace'

    os.chdir('/workspace')

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
                    print(f'Fetching dependency: {dep}')    
                    fetch_deps_recursive(dep)
        except IOError:
            print('No dependencies file for this repo.')
    else:
        print(f'Dependency {repo} already fetched.')
        
def main():
    repo = sys.argv[1]

    fetch_deps_recursive(repo)

if __name__ == "__main__":
    main()