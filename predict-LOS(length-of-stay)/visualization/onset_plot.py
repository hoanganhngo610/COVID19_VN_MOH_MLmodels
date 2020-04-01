import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

path = 'df_total.csv'
data = pd.read_csv(path)

onset_fever = data.iloc[:, 9:10].values
onset_cough = data.iloc[:, 10:11].values
onset_tired = data.iloc[:, 11:12].values
onset_sorethroat = data.iloc[:, 12:13].values
onset_respiratory = data.iloc[:, 13:14].values

onset_fever = np.reshape(onset_fever, len(onset_fever))
onset_cough = np.reshape(onset_cough, len(onset_cough))
onset_tired = np.reshape(onset_tired, len(onset_tired))
onset_sorethroat = np.reshape(onset_sorethroat, len(onset_sorethroat))
onset_respiratory = np.reshape(onset_respiratory, len(onset_respiratory))

onset_total = np.sum((onset_fever, onset_cough, onset_tired, onset_sorethroat, onset_respiratory), axis=0).tolist()
onset_fever = onset_fever.tolist()
onset_cough = onset_cough.tolist()
onset_tired = onset_tired.tolist()
onset_sorethroat = onset_sorethroat.tolist()
onset_respiratory = onset_respiratory.tolist()

count0_fever = onset_fever.count(0)
count1_fever = onset_fever.count(1)
count_fever = [count0_fever, count1_fever]

count0_cough = onset_cough.count(0)
count1_cough = onset_cough.count(1)
count_cough = [count0_cough, count1_cough]

count0_tired = onset_tired.count(0)
count1_tired = onset_tired.count(1)
count_tired = [count0_tired, count1_tired]

count0_sorethroat = onset_sorethroat.count(0)
count1_sorethroat = onset_sorethroat.count(1)
count_sorethroat = [count0_sorethroat, count1_sorethroat]

count0_respiratory = onset_respiratory.count(0)
count1_respiratory = onset_respiratory.count(1)
count_respiratory = [count0_respiratory, count1_respiratory]

count0_total = onset_total.count(0)
count1_total = onset_total.count(1)
count2_total = onset_total.count(2)
count3_total = onset_total.count(3)
count4_total = onset_total.count(4)
count_total = [count0_total, count1_total, count2_total, count3_total, count4_total]

objects = ('0', '1')
objects_total = ('0', '1', '2', '3', '4')

fig, axs = plt.subplots(2, 3, sharex=True, sharey=True)
axs[0, 0].bar(objects, count_fever, color='darkblue', edgecolor='black', width=0.6, align='center', alpha=0.6)
axs[0, 0].set_title('ONSET_FEVER')
axs[0, 1].bar(objects, count_cough, color='darkblue', edgecolor='black', width=0.6, align='center', alpha=0.6)
axs[0, 1].set_title('ONSET_COUGH')
axs[0, 2].bar(objects, count_tired, color='darkblue', edgecolor='black', width=0.6, align='center', alpha=0.6)
axs[0, 2].set_title('ONSET_TIRED')
axs[1, 0].bar(objects, count_sorethroat, color='darkblue', edgecolor='black', width=0.6, align='center', alpha=0.6)
axs[1, 0].set_title('ONSET_SORETHROAT')
axs[1, 1].bar(objects, count_respiratory, color='darkblue', edgecolor='black', width=0.6, align='center', alpha=0.6)
axs[1, 1].set_title('ONSET_RESPIRATORY')
axs[1, 2].bar(objects_total, count_total, color='darkblue', edgecolor='black', width=0.6, align='center', alpha=0.6)
axs[1, 2].set_title('ONSET_TOTAL')
for ax in axs.flat:
    ax.set(ylabel='Total cases')
# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in axs.flat:
    ax.label_outer()
    
plt.show()