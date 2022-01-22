import json
import sys
import yaml


def main(manifest_file, output_file, pod_name):

    try:
        with open(manifest_file, 'r') as file:
            manifest_object = yaml.safe_load(file)
    except OSError:
        print("Error reading manifest file")
        sys.exit(1)        

    repo_list = []
    pod_list = list(filter(lambda pod: pod['name'] == pod_name, manifest_object['integrationservers']))

    if(len(pod_list) == 0):
        print(f'Could not find integration server {pod_name} in manifest file.')
        sys.exit(1)

    pod = pod_list.pop()

    for app in pod['repositories']:
        repo_list.append(app)

    with open(output_file, 'w') as file:
        json.dump(repo_list, file)

main(sys.argv[1], sys.argv[2], sys.argv[3])