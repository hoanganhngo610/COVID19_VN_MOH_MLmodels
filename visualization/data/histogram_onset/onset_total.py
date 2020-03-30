import numpy as np
import pandas as pd 
from matplotlib import pyplot as plt

path = './predict-LOS(length-of-stay)/assets/processed/df_total.csv'
data = pd.read_csv(path)

onset_fever = data.iloc[:, 8:9].values
onset_cough = data.iloc[:, 9:10].values
onset_tired = data.iloc[:, 10:11].values
onset_throat = data.iloc[:, 11:12].values
onset_res = data.iloc[:, 12:13].values

onset_fever = np.reshape(onset_fever, len(onset_fever))
onset_cough = np.reshape(onset_cough, len(onset_cough))
onset_tired = np.reshape(onset_tired, len(onset_tired))
onset_throat = np.reshape(onset_throat, len(onset_throat))
onset_res = np.reshape(onset_res, len(onset_res))

onset_total = np.sum((onset_fever, onset_cough, onset_tired, onset_throat, onset_res), axis=0).tolist()

count0 = onset_total.count(0)
count1 = onset_total.count(1)
count2 = onset_total.count(2)
count3 = onset_total.count(3)
count4 = onset_total.count(4)
count = []
count.append(count0)
count.append(count1)
count.append(count2)
count.append(count3)
count.append(count4)

objects = ('0', '1', '2', '3', '4')

plt.bar(objects, count, color='darkblue', edgecolor='black', width=0.6, align='center', alpha=0.5)
plt.title('ONSET_TOTAL occurence', fontsize=20)
plt.xlabel('ONSET_TOTAL', fontsize=14)
plt.show()