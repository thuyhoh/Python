import matplotlib as plt
import numpy as np

t = np.linspace(0,1,1000)
A = 2
f0 = 5
x = A*np.cos(2*np.pi*f0*t)
plt.plot(t,x,"-b")
plt.title(r"$x(t) = 2\cos(2\pi 5t)$")
plt.xlabel(r"t (in s)")
plt.grid()
plt.tight_layout()
plt.show()

np.arange()