import matplotlib.pyplot as plt
import numpy as np
import math 

# tao du lieu de ve do thi 
x = np.arange(0,math.pi*2,0.05)

fig = plt.figure()
axes1 = fig.add_axes([0,0,1,1])
axes2 = fig.add_axes([0,0,1,1])
y1 = np.sin(x)
y2 = np.cos(x)
axes1.plot(x,y1)
axes2.plot(x,y2)

axes1.set_title("duong sine")
axes2.set_title("duong cosine")
plt.show()