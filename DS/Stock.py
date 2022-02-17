import json
 
# Opening JSON file
f = open('stocks.json')
 
# returns JSON object as
# a dictionary
data = json.load(f)
 
# Iterating through the json
# list
for i in data['Equity']:
    print(i)
 
# Closing file
f.close()