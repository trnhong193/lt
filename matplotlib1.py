
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
path = r'/home/hongnee/Downloads/california_housing_train.csv'
df = pd.read_csv(path)
xpoints = np.array(df['total_bedrooms'])
ypoints = np.array(df['median_house_value'])
plt.plot(xpoints, ypoints,)
plt.show()
#2
x = np.linspace(0,6)
y1 = 5*x
y2 = x**2
# y3 = np.exp(2*x)
plt.plot(x,y1,"-b",label = "y1")
plt.plot(x,y2,":r",label = "y2")
# plt.plot(x,y3,"k",label = "y3")
plt.legend(loc = "upper left")
plt.show()