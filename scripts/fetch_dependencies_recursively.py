import sys
import os
import json

def fetch_deps_recursive(repo):
    url = f'https://github.com/tineikt/{repo}.git'
    workspace = 'common-workspace'

    print('Currently in: ' + os.getcwd())

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
                print(dep)
                if dep:
                    fetch_deps_recursive(dep)
        except IOError:
            print('No dependencies file for this repo.')
    else:
        print(f'Dependency {repo} already cloned.')
        
def main():
    repo = sys.argv[1]

    fetch_deps_recursive(repo)

if __name__ == "__main__":
    main()