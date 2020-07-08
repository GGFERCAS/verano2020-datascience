
import pandas as pd
from matplotlib import pyplot

meteorites = pd.read_csv("meteorites.csv")

figures, axes = pyplot.subplots()


def map_value(value, min_value, max_value, lower, upper):
    return (value - min_value) / (max_value- min_value) * (upper - lower) + lower

sizes = []

for mass in meteorites["mass (g)"]:
    size = map_value(mass, 0, 6000000, 1, 200)
    sizes.append(size)

axes.scatter(meteorites.year, meteorites.reclat)
pyplot.show

