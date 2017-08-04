import json
from urllib.parse import quote
import urllib.request
import random

key = 'YOUR_GOOGLE_API_KEY'
query = str(input('Enter your query '))

query = quote(query)
url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query=' + query  + '&key=' + key
print('Your url is ' + url)
print('\n==================================\n')

response = urllib.request.urlopen(url)
data = response.read()
encoding = response.info().get_content_charset('utf-8')
jsonObject = json.loads(data.decode(encoding))


for i in range(0,len(jsonObject['results'])):

    tempJsonObject = jsonObject['results'][i]
    try:
        print(tempJsonObject['name'])
        print(tempJsonObject['rating'])
        print(tempJsonObject['formatted_address'])
    except:
        continue

    print('\n==================================')

print('==================================')
print('==================================')
print('==================================')
print('The computer has decided you will go to ')
choiceOfRestaurant = jsonObject['results'][random.randint(0,len(jsonObject['results']))]

print(choiceOfRestaurant['name'])
print(choiceOfRestaurant['rating'])
print(choiceOfRestaurant['formatted_address'])

print('\n==================================')
print('==================================')
print('==================================')
print('Other results above')

