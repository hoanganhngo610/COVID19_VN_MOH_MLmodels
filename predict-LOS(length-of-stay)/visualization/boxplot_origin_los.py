import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

path = 'df_train.csv'
data = pd.read_csv(path)

filter_europe = data.loc[data['ORIGIN_EUROPE'] == 1]
filter_china = data.loc[data['ORIGIN_CHINA'] == 1]
filter_us = data.loc[data['ORIGIN_US'] == 1]
filter_asean = data.loc[data['ORIGIN_ASEAN'] == 1]
filter_domestic = data.loc[data['ORIGIN_DOMESTIC'] == 1]

def get_los(filter_origin):
    los = filter_origin.iloc[:, 17:].values
    return np.reshape(los, len(los)).tolist()

los_europe = get_los(filter_europe)
los_china = get_los(filter_china)
los_us = get_los(filter_us)
los_asean = get_los(filter_asean)
los_domestic = get_los(filter_domestic)

combine_los = [los_europe, los_china, los_us, los_asean, los_domestic]

plt.boxplot(combine_los)
plt.xticks([1, 2, 3, 4, 5], ['EUROPE', 'CHINA', 'US', 'ASEAN', 'DOMESTIC'], fontsize=14)
plt.ylabel('Length of stay', fontsize=20)
plt.yticks(fontsize=14)
plt.title('Length of stay with respect to origin', fontsize=24)
plt.show()