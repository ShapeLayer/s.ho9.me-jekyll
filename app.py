from json import loads
from os import mkdir, path

links = loads(open('links.json', encoding='utf-8').read())

for config in links:
    template = open('./templates/{}.md'.format(config['template']), encoding='utf-8').read()
    for c in config:
        value = config[c]
        if c == 'date':
            if config[c] == 'default':
                value = '0000-00-00 00:00:00 +0900'
        template = template.replace('##_{name}_##'.format(name=c), value)
    with open('./docs/_posts/{}.md'.format(config['filename']), 'w', encoding='utf-8') as f:
        f.write(template)