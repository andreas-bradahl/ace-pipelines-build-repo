import json
import pytest

from get_repo_list import *


def test_store_repo_names():
    """Test that the created list is the same as the expected list."""
    with open('testfiles/github_payload.json') as file:
        resp_dict = json.load(file)

    actual = store_repo_names(resp_dict)
    expected = ['petstore', 'petstore-config']
    
    # Sort so that the order of elements doesn't matter
    assert actual.sort() == expected.sort()


def test_store_repo_names_empty_dict():
    """Test that a KeyError is thrown when sending an empty list to store_repo_names"""
    with pytest.raises(KeyError):
        empty_dict = {}

        actual = store_repo_names(empty_dict)
        expected = []

        assert actual == expected


def test_write_repos_to_file_assert_content():
    """"Test that the file written has the expected format"""
    repo_list = ['repo1', 'repo2', 'repo3']
    filename = 'repos/repo_list.json'
    expected = '["repo1", "repo2", "repo3"]'

    write_repos_to_file(repo_list, filename)
    
    with open(filename, 'r') as f:
        assert f.read() == expected
