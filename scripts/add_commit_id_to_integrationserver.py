import sys

from yaml import safe_load, dump

commit_id = sys.argv[1]
integration_server_file = sys.argv[2]
project_name = sys.argv[3]

try:
    with open(integration_server_file, 'r') as infile:
        integration_server_object = safe_load(infile)
except FileNotFoundError:
    print('IntegrationServer manifest file not found - aborting ...')
    sys.exit(1)
except:
    print('Error when reading IntegrationServer manifest file - aborting ...')
    sys.exit(1)

try:
    image_id = integration_server_object['spec']['pod']['containers']['runtime']['image']
    new_image_id = image_id.split(':')[0] + ':' + image_id.split(':')[1] + f':{commit_id}'
    integration_server_object['spec']['pod']['containers']['runtime']['image'] = new_image_id
except KeyError:
    print('No valid image reference found in IntegrationServer manifest file.')
    print('Should be under spec.pod.containers.runtime.image - aborting ...')
    sys.exit(1)

try:
    with open(integration_server_file, 'w') as outfile:
        dump(integration_server_object, outfile)
except:
    print('Error when writing to IntegrationServer manifest file - aborting ... ')
    sys.exit(1)