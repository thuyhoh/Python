import matplotlib.pyplot as plt

# tao kieu du lieu de ve 
y = [1,4,9,16,25,36,49,64]
x1 = [1,16,30,42,55,68,77,88]
x2 = [1,6,12,18,28,40,52,65]

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
line1 = ax.plot(x1,y)
line2 = ax.plot(x2,y)

ax.legend(labels = ("duong 1","duong 2"),loc  = "lower right")
ax.set_title("ten hinh ve")
ax.set_xlabel("truc x")
ax.set_ylabel("truc y")
plt.show()