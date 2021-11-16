import xml.etree.ElementTree as ET
import json
import sys

project_folder = sys.argv[1]
tree = ET.parse(f'{project_folder}/.project')
root = tree.getroot()

deps_list = []
for project in root.find('projects'):
    deps_list.append(project.text)

print(deps_list)

with open('dependencies.json', 'w') as deps_file:
    json.dump(deps_list, deps_file)