import requests
import json


def store_repo_names(response_dictionary):
    """Returns a list of repo names in the GH payload dictionary"""
    repos = [value['name'] for value in response_dictionary['items']]
    
    return repos

def write_repos_to_file(repo_list, file_path):
    """Stores list of repo names to a file line by line"""
    with open(file_path, 'w') as file:
        for repo in repo_list:
            file.writelines(repo + '\n')
    
def execute_github_request(topic_name):
    """Executes an http request to the GH API - finds repos which contains the parameter 'topic_name' in its topics"""
    url = f"https://api.github.com/search/repositories?q=user:andreas-bradahl+topic:{topic_name}"
    user = 'andreas-bradahl'
    token = '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'

    response = requests.get(url, auth=(user, token))

    return response

def main():
    response = execute_github_request('petstore-topic')

    repo_list = store_repo_names(response.json())

    write_repos_to_file(repo_list, 'repos_test.txt')

if __name__ == '__main__':
    main()