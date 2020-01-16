#Farhana Roslan and Koshi Murakoshi

import json
import csv

#1.	Reads superheroes.json (in this folder)
with open('superheroes.json', 'r') as f:
    superheroes = json.load(f)
    
print(superheroes)

#Creates an empty array called powers
powers = []

#Loop thorough the members of the squad,
#and append the powers of each to the powers array.

members = superheroes['members']

for hero in members:
	powers.append(hero['powers'])

#Prints those powers to the terminal
print(powers)

#===========================================================================

#2. Write a header to the csv file
with open('superheroes.csv', 'w') as f:
	writer = csv.writer(f)
	writer.writerow(['Name', 'Age', 'Secret Identity', 'Powers', 'Squad Name', 'Hometown', 'Year Formed', 'Secret Base', 'Active'])

#3. Loop over the members, and for each member write a row to the csv file		
	members = superheroes['members']

	for hero in members:
		writer.writerow([hero["name"], hero["age"], hero["secretIdentity"], hero["powers"], superheroes['squadName'], superheroes['homeTown'], superheroes['formed'], superheroes['secretBase'], superheroes['active']])


