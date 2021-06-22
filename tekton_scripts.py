import requests
import json


def store_repo_names(response_dictionary):
    # Store list of repo names with given topic
    repos = [value['name'] for value in response_dictionary['items']]
    
    return repos

def write_repos_to_file(repo_list, file_path):
    # Print list of repo names to file
    with open(file_path, 'w') as file:
        for repo in repo_list:
            file.writelines(repo + '\n')
    
def execute_github_request(topic_name):
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