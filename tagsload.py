import json
from api.models import CSUClass, CSUTags

with open('SUM22tags.json') as infile:
    jsonin = json.load(infile)

for section in jsonin:
    secclassobj = CSUClass.objects.filter(cid=section['cid'], semester=section['semester'], subject=section['subject'])[0]
    match section['tag']:
        case 'CC':
            tagnm = 'Core Choice'
        case 'TE':
            tagnm = 'Technical Elective'
        case 'WAC':
            tagnm = 'Writing Across the Curriculum'
    secclassobj.csutags_set.create(tagname=tagnm, tagabbr=section['tag'])
