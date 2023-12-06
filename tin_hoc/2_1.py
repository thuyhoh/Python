import matplotlib.pyplot as plt
import numpy as np
import math

# Tao cac du lieu ve
x = np.arange(0,2*np.pi,0.001)
y = np.sin(x)

# ve duong
plt.plot(x,y)

# Them cac chu thich cho cac truc
plt.xlabel("goc")
plt.ylabel("sine")
plt.title("song sine")

# hien thi hinh da ve
plt.show()