import math
import numpy as np
import matplotlib.pyplot as Fiz423

# value range of speed (c).
x = np.arange(-1.0000, 1.0000, 0.0001)

# Lorentz function.
y = 1/np.sqrt(1-pow(x,2)/pow(1,2))

# create plot and set colors.
Fiz423.plot(x, y, "r", x, y, "b.")

# label of x axis.
Fiz423.xlabel("speed (c)")

# label of y axis.
Fiz423.ylabel("Lorentz Factor (gamma)")

# add grid.
Fiz423.grid(True)

# and show the plot.
Fiz423.show()
