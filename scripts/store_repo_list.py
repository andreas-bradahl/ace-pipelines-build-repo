import requests
import sys
import os
import json


def store_repo_names(response_dictionary):
    """Returns a list of repo names in the GH payload dictionary"""
    repos = [value['name'] for value in response_dictionary['items']]
    
    return repos


def write_repos_to_file(repo_list, filename):
    """Stores list of repo names to a file line by line"""
    
    # Create folder structure if it doesn't exist
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, 'w') as file:
        file.write(json.dumps(repo_list))

    
def execute_github_request(topic_name):
    """Executes an http request to the GH API - finds repos which contains the parameter 'topic_name' in its topics"""
    url = f"https://api.github.com/search/repositories?q=user:andreas-bradahl+topic:{topic_name}"
    # user = os.environ.get('GITHUB_USER')
    # token = os.environ.get('GITHUB_TOKEN')

    # response = requests.get(url, auth=(user, token))
    response = requests.get(url)

    # Write payload to test file
    # with open('testfiles/github_payload.json', 'w') as f:
    #     f.write(json.dumps(response.json()))

    return response


def main():
    if len(sys.argv) == 2:
        arguments = sys.argv[1].split()
        topic = arguments[0]
        repo_list_filepath = arguments[1]

        response = execute_github_request(topic)
        print(response.status_code)

        repo_list = store_repo_names(response.json())
        print(repo_list)

        repo_list_path = f'{repo_list_filepath}'

        write_repos_to_file(repo_list, repo_list_path)
    elif len(sys.argv) > 3:
        print("Error: Too many arguments.")
    else:
        print("Error: No GitHub topic argument received.")


if __name__ == '__main__':
    main()