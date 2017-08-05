import json
from urllib.parse import quote
import urllib.request
import random

key = 'YOUR_GOOGLE_API_KEY'
query = str(input('What are you looking for? '))

# Makes sure input given for query is good for url
query = quote(query)

# Makes url with given information
url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query=' + query + '&key=' + key
print('Your url is ' + url)
print('\n==================================')

# Fetches json from url and converts it into a json object
response = urllib.request.urlopen(url)
data = response.read()
encoding = response.info().get_content_charset('utf-8')
jsonObject = json.loads(data.decode(encoding))

# Goes through json object to fetch every location
for i in range(0, len(jsonObject['results'])):

    # Every location is made into a json object which will then be parsed
    tempJsonObject = jsonObject['results'][i]
    # In a try block in case there is no name, rating or address
    try:
        print(tempJsonObject['name'])
        print(tempJsonObject['rating'])
        print(tempJsonObject['formatted_address'])
    except:
        continue

    print('\n==================================')

# Selects random place from json and parses it and prints it
print('==================================\n' * 3)
print('The computer has decided you will go to ')
choiceOfRestaurant = jsonObject['results'][random.randint(0, len(jsonObject['results']))]
# Same reason for the try block as before
try:
    print(choiceOfRestaurant['name'])
    print(choiceOfRestaurant['rating'])
    print(choiceOfRestaurant['formatted_address'])
except:
    print('Trouble fetching some data')

print('\n' + ('==================================\n' * 3))
print('Other results above')
