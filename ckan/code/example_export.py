from ckanapi import RemoteCKAN

ckan = RemoteCKAN('http:/............', apikey='xxxxxxxxxxxxxxxxx')
dataset = ckan.action.package_search(include_private=True)

for data in dataset['results']:
    if data['private']:
        print "Privat,", data['title']
    else:
        print "Publik,", data['title']
