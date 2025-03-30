"""
import json
with open('nobel_prizes.json', 'r') as nob:
    data = json.load(nob)

import pprint

years = {
    '2014' : 0,
    '2015' : 0,
    '2016' : 0,
    '2017' : 0,
    '2018' : 0,
    '2019' : 0,
    '2020' : 0,
    '2021' : 0,
    '2022' : 0,
    '2023' : 0,
    '2024' : 0,
}
for i, prize in enumerate(data["prizes"]):
    for year in years:
        if year in prize['year'] and prize['category'] == "economics":
            years[year] += len(prize['laureates'])
pprint.pprint(years)


terms = list(years.keys())
counts = list(years.values())

sorted_terms = []
sorted_counts = []
for term in sorted(terms):
    sorted_terms.append(term)
    sorted_counts.append(years[term])

import matplotlib.pyplot as plt
plt.bar(sorted_terms, sorted_counts)
plt.xlabel("Year")
plt.ylabel("Number of Economics Nobel Prize Recipients")
plt.title("Number of Recipents of the Nobel Prize in Economics (2014-2024)")
plt.show()
"""

import pprint
import csv
import numpy as np


x_values = []
y_values1 = []
y_values2 = []


with open('vehicle_counts.csv', 'r') as csvfile:
    vehicles = csv.reader(csvfile, delimiter = ',')
    for row in vehicles:
        if row[1] == "Montana":
            x_values.append(row[0])
            y_values1.append(float(row[2]))
            y_values2.append(float(row[4]))


import matplotlib.pyplot as plt
plt.plot(x_values, y_values1, color= 'g', marker = "o", label = "Cars")
plt.plot(x_values, y_values2, color= 'b', marker = "o", label = "Motorcycles")

plt.yticks(range(5000, 121000, 10000))
plt.xticks(rotation = 25)
plt.xlabel('Year')
plt.ylabel('Number of Vehicles Registered')
plt.title('Amount of Vehicles Registered in Montana, 1920-1929')
plt.legend()
plt.show()



