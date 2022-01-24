import sys

from yaml import safe_load, dump

commit_id = sys.argv[1]
integration_server_file = sys.argv[2]
event_repo = sys.argv[3]

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
    integration_server_object['metadata']['labels']['lastEventCommitId'] = commit_id
except KeyError:
    print('Could not find tag lastEventCommitId.')
    print('Should be under metadata.labels.lastEventCommitId - aborting ...')
    sys.exit(1)

try:
    integration_server_object['metadata']['labels']['lastEventRepo'] = event_repo
except KeyError:
    print('Could not find tag lastEventRepo.')
    print('Should be under metadata.labels.lastEventRepo - aborting ...')
    sys.exit(1)    

try:
    with open(integration_server_file, 'w') as outfile:
        dump(integration_server_object, outfile)
except:
    print('Error when writing to IntegrationServer manifest file - aborting ... ')
    sys.exit(1)