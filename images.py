import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
from matplotlib.path import Path
from matplotlib.patches import PathPatch

A = np.random.rand(5, 5)

axe = plt.plot()
interp = 'bilinear'
plt.imshow(A, interpolation=interp)
plt.title(interp.capitalize())
plt.grid(True)
plt.show()

