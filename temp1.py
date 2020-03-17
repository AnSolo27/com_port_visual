import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate
x = np.arange(-5.01, 5.01, 0.25)
y = np.arange(-5.01, 5.01, 0.25)
xx, yy = np.meshgrid(x, y)
z = np.sin(xx**2+yy**2)
print("z len  = ", len(z))
f = interpolate.interp2d(x, y, z, kind='cubic')
xnew = np.arange(-5.01, 5.01, 0.01)
ynew = np.arange(-5.01, 5.01, 0.01)
znew = f(xnew, ynew)
print("z new len  = ", len(znew))
plt.plot(xnew, znew[0,:])
plt.show()