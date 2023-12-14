import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1,5,10,15,20,30])
ypoints = np.array([3,10,3,10,3,20])


plt.figure(figsize=(5,5))
plt.plot(xpoints,ypoints, color='green')
plt.xlim([0,30])
plt.ylim([0,30])
plt.show()