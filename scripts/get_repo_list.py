import requests
import sys
import os
import json


def get_repo_names(response_dictionary):
    """Returns a list of repo names in the GH payload dictionary"""
    repos = [value['name'] for value in response_dictionary['items']]

    print(f"Found {len(repos)} repositories:")
    for repo in repos:
        print(repo)

    return repos


def write_repos_to_file(repo_list, filename):
    """Stores list of repo names to a file"""

    # Create folder structure if it doesn't exist
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, 'w') as file:
        file.write(json.dumps(repo_list))


def execute_github_request(user, topic):
    """Executes an http request to the GH API - finds repos which contains the parameter 'topic_name' in its topics"""
    print(f'Find repos in user/org: {user}, with topic: {topic}')
    url = f"https://api.github.com/search/repositories?q=user:{user}+topic:{topic}"
    # user = os.environ.get('GITHUB_USER')
    # token = os.environ.get('GITHUB_TOKEN')

    # response = requests.get(url, auth=(user, token))
    response = requests.get(url)

    return response


def main():
    NUMBER_OF_ARGUMENTS = 3

    if len(sys.argv) == NUMBER_OF_ARGUMENTS:
        user = sys.argv[1]
        topic = sys.argv[2]

        response = execute_github_request(user, topic)
        repo_list = get_repo_names(response.json())
        absolute_path = os.getcwd()
        write_repos_to_file(repo_list, absolute_path + 'repos/repos.json')
    elif len(sys.argv) > NUMBER_OF_ARGUMENTS:
        print("Error: Too many arguments")
    else:
        print("Error: No GitHub topic argument received.")

if __name__ == '__main__':
    main()
