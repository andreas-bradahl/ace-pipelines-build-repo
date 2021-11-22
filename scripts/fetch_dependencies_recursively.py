import sys
import os
import json

def fetch_deps_recursive(repo):
    url = f'https://github.com/tineikt/{repo}.git'

    print('Currently in: ' + os.getcwd())

    os.chdir('/workspace')

    clone = f'git clone -b cicd {url} common-workspace/{repo}'
    os.system(clone)
    os.chdir(f'common-workspace/{repo}')
    
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
        
def main():
    repo = sys.argv[1]

    fetch_deps_recursive(repo)

if __name__ == "__main__":
    main()