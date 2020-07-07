
import math

from matplotlib import pyplot


x_coords = range(1, 11)
y_coords = [math.sin(x) for x in x_coords]
pyplot.plot(x_coords, y_coords)
# pyplot.plot(x_coords, y_coords)

# pyplot.xlim(0, 10)
# pyplot.ylim(-5, 10)
pyplot.show()

# pyplot.savefig("output.png")