import json

with open('united-states.json') as f:
    data = json.load(f)

print(data)
#converting the json in another file to a python dictionary

#print out the states names
#print(data['states'])
for state_name in data['states']:
    print(state_name['name']+ ":" + state_name['abbreviation']) 

with open('new-file.json', 'w') as f:
    json.dump(data, f, indent=2)