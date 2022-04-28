import json
with open('megajson.json') as jsonin:
    unfilteredobj = json.load(jsonin)
    count = 0
    for semester in unfilteredobj:
        for x in semester:
            print(f"Class ID: {x['cid']}")
            count += 1
        print(f'\t{len(semester)}')
    print(count)