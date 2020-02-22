# Run this script to generate a README file that contains version info

import yaml

sources = yaml.safe_load(open("./docs-source.yml", encoding="utf8").read())
with open('docs/README.md', mode='w') as readme:
    readme.write('# Docs Version\n\n')
    for source in sources:
        name = source['name']
        uri = source['uri']
        docs_commit_id = source['commit-id-of-last-update']
        docs_link = source['docs_uri'].replace('{commit-id}', docs_commit_id)
        readme.write(f"- [{name}]({uri}) at [{docs_commit_id}]({docs_link}).\n")
