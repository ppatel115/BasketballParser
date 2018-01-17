import json
from pprint import pprint

data = json.load(open('pbp_cincinnati.json'))

for i in range(0,10):
    pprint(data["periods"][0]['playStats'][i])
    # pprint(data["periods"][0]['playStats'][i]['visitorText'])
