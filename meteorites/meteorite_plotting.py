# import matplotlib as plt
from matplotlib import pyplot
from meteorite_data import meteorites
from collections import defaultdict


counts = defaultdict(int)
for meteor in meteorites:
    year = meteor["year"][6:10]
    counts[year] += 1

amaunt = 2
x_values = list(counts.keys())[:amaunt]
y_values = list(counts.values())[:amaunt]

pyplot.bar(x_values, y_values)
pyplot.show()