import json

with open("./data.json") as f:
    dic = json.load(f);

ric = {}
for line in dic:
    #ric[line['alpha-3']] = {}
    ric[line['alpha-3']] = {}
    ric[line['alpha-3']]['name'] = line['name']

with open("code_to_country.json","w") as ou:
    json.dump(ric,ou,indent=4,sort_keys=True)
