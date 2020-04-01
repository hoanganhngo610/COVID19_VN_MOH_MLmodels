import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

path = 'df_total.csv'
data = pd.read_csv(path)

origin_europe = data.iloc[:, 3:4].values
origin_china = data.iloc[:, 4:5].values
origin_us = data.iloc[:, 5:6].values
origin_asean = data.iloc[:, 6:7].values
origin_domestic = data.iloc[:, 7:8].values

origin_europe = np.reshape(origin_europe, len(origin_europe))
origin_china = np.reshape(origin_china, len(origin_china))
origin_us = np.reshape(origin_us, len(origin_us))
origin_asean = np.reshape(origin_asean, len(origin_asean))
origin_domestic = np.reshape(origin_domestic, len(origin_domestic))

origin_total = np.sum((origin_europe, origin_china, origin_us, origin_asean, origin_domestic), axis=0).tolist()
origin_europe = origin_europe.tolist()
origin_china = origin_china.tolist()
origin_us = origin_us.tolist()
origin_asean = origin_asean.tolist()
origin_domestic = origin_domestic.tolist()

count0_europe = origin_europe.count(0)
count1_europe = origin_europe.count(1)
count_europe = [count0_europe, count1_europe]

count0_china = origin_china.count(0)
count1_china = origin_china.count(1)
count_china = [count0_china, count1_china]

count0_us = origin_us.count(0)
count1_us = origin_us.count(1)
count_us = [count0_us, count1_us]

count0_asean = origin_asean.count(0)
count1_asean = origin_asean.count(1)
count_asean = [count0_asean, count1_asean]

count0_domestic = origin_domestic.count(0)
count1_domestic = origin_domestic.count(1)
count_domestic = [count0_domestic, count1_domestic]

count0_total = origin_total.count(0)
count1_total = origin_total.count(1)
count2_total = origin_total.count(2)
count_total = [count0_total, count1_total, count2_total]

objects = ('0', '1')
objects_total = ('0', '1', '2')

fig, axs = plt.subplots(2, 3, sharex=True, sharey=True)
axs[0, 0].bar(objects, count_europe, color='darkblue', edgecolor='black', width=0.6, align='center', alpha=0.6)
axs[0, 0].set_title('ORIGIN_EUROPE')
axs[0, 1].bar(objects, count_china, color='darkblue', edgecolor='black', width=0.6, align='center', alpha=0.6)
axs[0, 1].set_title('ORIGIN_CHINA')
axs[0, 2].bar(objects, count_us, color='darkblue', edgecolor='black', width=0.6, align='center', alpha=0.6)
axs[0, 2].set_title('ORIGIN_US')
axs[1, 0].bar(objects, count_asean, color='darkblue', edgecolor='black', width=0.6, align='center', alpha=0.6)
axs[1, 0].set_title('ORIGIN_ASEAN')
axs[1, 1].bar(objects, count_domestic, color='darkblue', edgecolor='black', width=0.6, align='center', alpha=0.6)
axs[1, 1].set_title('ORIGIN_DOMESTIC')
axs[1, 2].bar(objects_total, count_total, color='darkblue', edgecolor='black', width=0.6, align='center', alpha=0.6)
axs[1, 2].set_title('ORIGIN_TOTAL')
for ax in axs.flat:
    ax.set(ylabel='Total cases')

# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in axs.flat:
    ax.label_outer()
plt.show()