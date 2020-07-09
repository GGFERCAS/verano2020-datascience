
import pandas as pd
import datetime
from matplotlib import pyplot


def parse_year_string(year_string):
    if not year_string:
        return 0
    
    if year_string[-1] == "M":
        format_pattern = "%m/%d/%Y %I:%M:%S %p"

    else:
        format_pattern = "%m/%d/%Y %H:%M:%S"

    return datetime.datetime.strptime(year_string, format_pattern).year

converters = {
    "year": parse_year_string
}

meteorites = pd.read_csv("meteorites.csv", converters=converters)

meteorites = meteorites[meteorites.year != 0]

figures, axes = pyplot.subplots()


def map_value(value, min_value, max_value, lower, upper):
    return (value - min_value) / (max_value- min_value) * (upper - lower) + lower

sizes = []

for mass in meteorites["mass (g)"]:
    size = map_value(mass, 0, 6000000, 1, 200)
    sizes.append(size)

axes.scatter(meteorites.year, meteorites.reclat, s=sizes, alpha=0.5)
pyplot.show()