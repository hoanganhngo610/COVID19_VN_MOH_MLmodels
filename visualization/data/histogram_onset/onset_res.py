import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

path = './predict-LOS(length-of-stay)/assets/processed/df_total.csv'
data = pd.read_csv(path)

onset = data.iloc[:, 12:13].values
onset = np.reshape(onset, len(onset)).tolist()
count0 = onset.count(0)
count1 = onset.count(1)
count = []
count.append(count0)
count.append(count1)

objects = ('0', '1')

plt.bar(objects, count, color='darkblue', edgecolor='black', width=0.6, align='center', alpha=0.5)
plt.title('ONSET_RES occurence', fontsize=20)
plt.xlabel('ONSET_RES', fontsize=14)
plt.show()