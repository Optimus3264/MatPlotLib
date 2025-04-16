import matplotlib.pyplot as plt
import numpy as np

x=np.array([35,25,25,15])
fruits=['Apple','Banana','Cherry','Dates']

plt.pie(x,labels=fruits,startangle=90)
plt.show()