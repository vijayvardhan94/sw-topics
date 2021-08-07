import json
# a python string that has a valid josn
person_string = '''
{
    "people":[
        {
            "name": "John Smith",
            "phone": "900-000-1234",
            "email": "john@hasemail.com",
            "has_id": true

        },
        {   "name": "John Doe",
            "phone": "100-000-1234", 
            "email": "doe@hasemail.com",
            "has_id": null

        }
    ]
}
'''
#loading the string into a python dictionary
#json.loads converts a string or json to a python object
data = json.loads(person_string)
print(data)
print(type(data))

print((data["people"]))
print((data["people"][0]))

for i in data['people']:
    print(i["name"] + " has been verified")

#json dump
json_string = json.dumps(data, indent=2, sort_keys = True)
print(json_string)
print(type(json_string))