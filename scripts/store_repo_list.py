import requests
import sys
import os


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
        response = execute_github_request(sys.argv[1])
        print(response.status_code)

        repo_list = store_repo_names(response.json())
        print(repo_list)

        write_repos_to_file(repo_list, 'repos_list.txt')
    elif len(sys.argv) > 2:
        print("Error: Too many arguments (only one GitHub topic allowed).")
    else:
        print("Error: No GitHub topic argument received.")

if __name__ == '__main__':
    main()