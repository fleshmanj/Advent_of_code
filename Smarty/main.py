import matplotlib.pyplot as plt
import matplotlib as mpl
from data import points



for k, v in points.items():
    plt.plot(v["lat"], v["long"])
plt.show()
