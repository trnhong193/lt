import pandas as pd
import numpy as np
path = r'/home/hongnee/Downloads/california_housing_train.csv'
df = pd.read_csv(path)
# #1
df_2 = df[['total_rooms','total_bedrooms','population','median_house_value']] #lay_cac_cot
# print(df_2)
df.to_csv('df_2')#luu
# #2
a = df_2['median_house_value'].idxmax() #lay_dia_chi_gt_max
b = df_2['median_house_value'].idxmin()
print(df_2.loc[a,:]) #lay_hang_dac_biet
print(df_2.loc[b])
#3
c = df['median_house_value'].mean()
print('Gia_tri_tb: ',c)
#4
df_4 = df[['total_bedrooms','median_house_value']]
#df_5 = df.loc[:,['total_bedrooms','median_house_value']]
so_hang =df_4.shape[0]
df_5=df_4.copy()
arr_4=np.array(df_4)
arr_5=np.array(df_5)
print(arr_5)
for i in range (2):
    for j in range (2,so_hang):
        arr_4[j][i] += arr_4[j-1][i] 
        # arr_4[j][i] = arr_5[j-1][i] + arr_5[j-2][i]
df_4=pd.DataFrame(arr_4)
print(df_4)