# Run this script to check update of docs source defined in data-source.yml

import sys
import requests
import yaml

sources = yaml.safe_load(open("./docs-source.yml", encoding="utf8").read())

all_source_is_up_to_date = True
for source in sources:
    if source['enable']:
        docs_uri = source['docs_uri']
        docs_master = requests.get(docs_uri.replace('{commit-id}', 'master')).text
        docs_last_update = requests.get(docs_uri.replace('{commit-id}', source['commit-id-of-last-update'])).text
        if docs_master != docs_last_update:
            print(f'docs of {source["name"]} is outdated.')
            all_source_is_up_to_date = False

if not all_source_is_up_to_date:
    sys.exit(1)
