import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

path = r'/home/hongnee/Downloads/chapter6_data/polynomial.csv'
hongne = pd.read_csv(path)
X = np.array(hongne['x']).T
y = np.array(hongne['y']).T
plt.plot(X,y,'r')
plt.show()