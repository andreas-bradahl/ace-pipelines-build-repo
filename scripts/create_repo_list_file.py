import json
import sys
import yaml


def main():
    manifest_file = sys.argv[1]
    file_path = sys.argv[2]

    with open(manifest_file, 'r') as file:
        manifest_object = yaml.safe_load(file)

    repo_list = []
    for app in manifest_object['repositories']:
        repo_list.append(app)

    with open(file_path, 'w') as file:
        json.dump(repo_list, file)

main()