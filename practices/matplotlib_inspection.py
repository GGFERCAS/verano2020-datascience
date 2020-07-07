
import math
import numpy as np

from matplotlib import pyplot


# Defined the values of x and y axes. Change the line colour.
x_coords = np.arange(1, 11, 0.001)
y_coords = [math.sin(x) for x in x_coords]

# Made a table using our x_coords and our y_coords.  Change the line colour.
pyplot.plot(x_coords, y_coords, "r")

# Made x and y axis limits
# pyplot.xlim(0, 10)
# pyplot.ylim(-5, 10)

# Set axis ticks
pyplot.xticks([1,2,3,4,5,6,7,8,9,10,11])
pyplot.yticks([-1, 0, 1])

# Extra Info

pyplot.xlabel('x-values')
pyplot.ylabel('y-values')
pyplot.title('MY TABLE!')


# Shows the table
pyplot.show()



# Save the table as a photo
# pyplot.savefig("output.png")