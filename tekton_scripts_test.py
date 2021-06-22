import json

from tekton_scripts import *

with open('github_payload.json') as file:
    resp_dict = json.load(file)

def test_store_repo_names():
    """Test that the created list is the same as the expected list."""
    actual = store_repo_names(resp_dict)
    expected = ['petstore', 'petstore-config']
    assert actual == expected

def test_write_repos_to_file_number_of_lines_is_three():
    """"Test that the file written has the expected format"""
    repo_list = ['repo1', 'repo2', 'repo3']

    write_repos_to_file(repo_list, 'repos_test.txt')
    
    with open('repos_test.txt', 'r') as f:
        assert f.readlines() == ['repo1\n', 'repo2\n', 'repo3\n']
