from asyncore import read
from api.models import CSUClass
from pprint import pprint
import json
from datetime import datetime
from decimal import Decimal

unfilteredobj = None
with open('sum22pack.json') as jsonin:
    unfilteredobj = json.load(jsonin)

def verify(targettype, dtstring):
    if dtstring == "None":
        return None
    else:
        if targettype == "bigdate":
            return datetime.strptime(dtstring, "%m/%d/%Y").date()
        elif targettype == "smalldate":
            return datetime.strptime(dtstring, "%m/%d/%y").date()
        elif targettype == "time":
            return datetime.strptime(dtstring, "%I:%M %p").time()
##exec(open('load.py').read())
for semester in unfilteredobj:
    for class_section in semester: 
        tstart = verify("time", class_section['begt'])
        tend = verify("time", class_section['endt'])
        dstart = verify("smalldate", class_section['begd'])
        dend = verify("smalldate", class_section['endd'])
        lastadd = verify("bigdate", class_section['Last Day To Add:'])
        lastdrop = verify("bigdate", class_section['Last Day To Drop:'])
        lastwithdraw = verify("bigdate", class_section['Last Day To Withdraw:'])
        if "specialtopic" not in class_section:
            class_section["specialtopic"] = "None"

        newClass = CSUClass(
            cid = class_section['cid'],
            name = class_section['name'],
            subject = class_section['subject'],
            semester = class_section['semester'],
            section = class_section['sec'],
            session = class_section['Session:'],
            begindate = dstart,
            enddate = dend,
            timestart = tstart,
            timeend = tend,
            location = class_section['room'],
            instructor = class_section['inst'],
            classtype = class_section['comp'],
            openstatus = class_section['stat'],
            enrolled = class_section['enrl'],
            capacity = class_section['capc'],
            credits = Decimal(class_section['Credits:']),
            consent = class_section['Consent:'],
            lastadddate = lastadd,
            lastdropdate = lastdrop,
            lastwithdrawdate = lastwithdraw,
            desc = class_section['desc'],
            specialtopic = class_section["specialtopic"]
        )
        newClass.save()
        for day in class_section['days']:
            newClass.csuclassdays_set.create(day = day)