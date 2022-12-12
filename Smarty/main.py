import matplotlib.pyplot as plt
import matplotlib as mpl
from data import points

x=[]
y=[]

for k, v in points.items():
    x.append(v["lat"])
    y.append(v["long"])
plt.plot(x,y)
plt.show()
