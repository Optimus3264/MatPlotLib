import matplotlib.pyplot as plt
import numpy as np

x=np.array(['a','b','c','d'])
y=np.array([3,8,1,10])

plt.barh(x,y,height=0.5)
plt.show()