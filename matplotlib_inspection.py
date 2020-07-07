
import math
import numpy as np

from matplotlib import pyplot


x_coords = np.arange(1, 11, 0.001)
y_coords = [math.sin(x) for x in x_coords]
pyplot.plot(x_coords, y_coords)
# pyplot.plot(x_coords, y_coords)

# pyplot.xlim(0, 10)
# pyplot.ylim(-5, 10)

# pyplot.xticks([1,2,3,4,5,6,7,8,9,10,11])

pyplot.show()

# pyplot.savefig("output.png")