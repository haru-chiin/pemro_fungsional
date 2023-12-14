import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0,6])
ypoints = np.array([0,250])
x = np.array([6,12])
y = np.array([250,0])
plt.plot(xpoints,ypoints)
plt.plot(x,y)
plt.show()