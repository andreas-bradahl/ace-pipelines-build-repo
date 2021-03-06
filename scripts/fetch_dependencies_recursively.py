import sys
import os
import json

def fetch_deps_recursive(repo, branch, repos_working_dir):
    url = f'https://github.com/tineikt/{repo}.git'

    os.chdir(repos_working_dir)

    clone = f'git clone -b {branch} {url} {repos_working_dir}/{repo}'
    if not os.path.exists(f'{repos_working_dir}/{repo}'):
        os.system(clone)
        os.chdir(f'{repos_working_dir}/{repo}')
        
        try:
            with open('dependencies.json', 'r') as deps_file:
                data = deps_file.read()
            
            dependencies = json.loads(data)
            for dep in dependencies:
                if dep:   
                    fetch_deps_recursive(dep, branch, repos_working_dir)
        except FileNotFoundError:
            print(f'No dependencies file for {repo}.')
        except IOError:
            print(f'Error opening dependencies file for {repo}')
    else:
        print(f'Dependency {repo} already fetched.')
        
def main():
    repo = sys.argv[1]
    branch = sys.argv[2]
    repos_working_dir = sys.argv[3]

    fetch_deps_recursive(repo, branch, repos_working_dir)

if __name__ == "__main__":
    main()