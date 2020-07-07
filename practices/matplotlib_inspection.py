
import math
import numpy as np

from matplotlib import pyplot


# Defined x_coords and colours as red, yellob and blue
colours = "ryb"
x_coords = np.arange(1, 11, 0.001)

# Defined the value of y axe
for i in range(1, 4):
    y_coords = np.sin(x_coords + i) * i
    # Made a table using our x_coords and our y_coords.  Change the line colour.
    pyplot.plot(x_coords, y_coords, colours[i - 1] + "x")


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