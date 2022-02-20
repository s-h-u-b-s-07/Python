import json
 
f = open('stocks.json')  # Opening JSON file

data = json.load(f)  # returns JSON object as a dictionary

for i in data['Equity']: #itrating through json 
    print(i)

f.close() #close file