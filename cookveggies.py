#Koshi and Hana
import csv
import json

#Read vegetables.csv (see previous section) into a variable called vegetables.

with open('vegetables.csv', 'r') as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    vegetables = [dict(row) for row in rows]
    
#Print the variable vegetables.
print(vegetables)

#Write vegetables as a JSON file called vegetables.json. It should look like this:

with open('vegetables.json', 'w') as f:
    json.dump(vegetables, f)

