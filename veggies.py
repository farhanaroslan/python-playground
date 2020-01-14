#Farhana Roslan and Koshi Murakoshi

import csv

vegetables = [
 {"name": "eggplant", "color": "purple"},
 {"name": "tomato", "color": "red"},
 {"name": "corn", "color": "yellow"},
 {"name": "okra", "color": "green"},
 {"name": "arugula", "color": "green"},
 {"name": "broccoli", "color": "green"},
]

#In the loop, write the name of each vegetable and the color into a CSV called vegetables.csv 

with open('vegetables.csv', 'w') as f:
	writer = csv.writer(f)
	writer.writerow(['Name of Vegetable', 'Color'])
		
	for veg in vegetables:
		writer.writerow([veg["name"],veg["color"]])

