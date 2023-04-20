#main.py
import requests
import json
#make a request to a web server and store the results in response
from iterateOverADictionaryPackage.iterateOverADictionary import *
response = requests.get('https://developer.nps.gov/api/v1/parks?parkCode=acad&api_key=pfJKDXPzTykVL73ehnPyY8pkDQLjfq5cz5LqCkl3')
json_string = response.content
parsed_json = json.loads(json_string) # Now we have a python dictionary

#Invoke my function in the other module, pass it parsed_json

iterate_dictionary(parsed_json)

print(parsed_json)

print(parsed_json['data'][0]['description'])
print(parsed_json['data'][0]['directionsInfo'])

total = int(parsed_json['total']) # The number of parks that were returned
#I just want the Descriptions of the parks
for park in parsed_json['data']:
    print (park["description"])

