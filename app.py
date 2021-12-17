from json import loads
from os import mkdir, path

links = loads(open('links.json', encoding='utf-8').read())

for config in links:
    template = open('./templates/{}.md'.format(config['template']), encoding='utf-8').read()
    datetime_value = config['date']
    if config['date'] == 'default':
        datetime_value = '0000-00-00 00:00:00 +0900'
    for c in config:
        value = config[c] if c != 'date' else datetime_value
        template = template.replace('##_{key}_##'.format(key=c), value)
    with open('./docs/_posts/{datetime}-{name}.md'.format(datetime=datetime_value.split()[0], name=config['filename']), 'w', encoding='utf-8') as f:
        f.write(template)