import json

with open("united-states.json") as f:
    data = json.load(f)

print(data)

for state_name in data['states']:
    del(state_name['area_codes'])
print(data)


with open('edited-states.json', 'w') as f:
    json.dump(data, f, indent=2)