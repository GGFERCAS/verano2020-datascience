
import math
import numpy as np

from matplotlib import pyplot


# Defined x_coords and colours as red, yellob and blue
colours = "ryb"
x_coords = np.arange(1, 11, 0.001)

# Extract the figures and axes from pyplot
figures, axes = pyplot.subplots(ncols=1, nrows=3, sharex=True)


# Defined the value of y axe
for i in range(1, 4):
    y_coords = np.sin(x_coords + i) * i
    # Made a table using our x_coords and our y_coords.  Change the line colour.
    axes[i - 1].plot(x_coords, y_coords, colours[i - 1] + "x")
# region
# Made x and y axis limits
# pyplot.xlim(0, 10)
# pyplot.ylim(-5, 10)
# endregion



    # Set axis ticks

    axes[i - 1].set_xticks(np.arange(x_coords[0], x_coords[-1]))
    axes[i - 1].set_yticks([-1, 0, 1])

    # Extra Info

    axes[i - 1].set_xlabel('x-values', x=0.9, y=1)
    axes[i - 1].set_ylabel('y-values')
    axes[i - 1].set_title('MY TABLE! ' + str(i))
    figures.suptitle('All the graphs')

    axes[i - 1].set_ylim(-3.2, 3.2)
    # figures.tight_layout()

# Shows the table

pyplot.show()



# Save the table as a photo

# pyplot.savefig("output.png")