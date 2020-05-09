import json

with open("./data.json") as f:
    dic = json.load(f);

ric = {}
for line in dic:
    #ric[line['alpha-3']] = {}
    ric[line['name']] = {}
    ric[line['name']]['alpha-3'] = line['alpha-3']

with open("country_to_code.json","w") as ou:
    json.dump(ric,ou,indent=4,sort_keys=True)
