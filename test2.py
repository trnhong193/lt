import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
path = r'/home/hongnee/Training_Python_2022/test_data/winequality-white.csv'
df = pd.read_csv(path,  sep = ";")

print(df.head())
print(df['quality'])

df3 = df.mean(axis=0)
print(df3)

df2 = df['quality']
# print(df2)
a = np.array(df2)

sohang = df2.shape[0]
print(sohang)
c1=0
c2=0
c3=0
for i in range (1,sohang):
    if a[i]>=7:
        c1 +=1
    elif a[i]<=3: 
        c3 +=1
    else: 
        c2+=1


print("good: ", c1)
print("middle: ", c2)
print("bad: ",c3)

x = np.array([1,2,3,6])
y = np.array([1,4,7,8])
plt.plot(x,y)
plt.show()


x = np.array(["good", "middle", "bad"])
y = np.array([c1,c2,c3])
plt.bar(x,y)
plt.show() 

