import json
import sys
import yaml

def main():
    manifest_file = sys.argv[1]

    with open(manifest_file, 'r') as file:
        manifest_object = yaml.safe_load(file)

    repo_list = []
    for app in manifest_object['applications']:
        repo_list.append(app)

    with open('repo_list.json', 'w') as file:
        json.dump(repo_list, file)

main()