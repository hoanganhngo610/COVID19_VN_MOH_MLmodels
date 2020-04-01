import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

path = 'df_train.csv'
data = pd.read_csv(path)

filter_fever = data.loc[data['ONSET_FEVER'] == 1]
filter_cough = data.loc[data['ONSET_COUGH'] == 1]
filter_tired = data.loc[data['ONSET_TIRED'] == 1]
filter_sorethroat = data.loc[data['ONSET_SORETHROAT'] == 1]
filter_respiratory = data.loc[data['ONSET_RESPIRATORY'] == 1]

def get_los(filter_onset):
    los = filter_onset.iloc[:, 17:].values
    return np.reshape(los, len(los)).tolist()

los_fever = get_los(filter_fever)
los_cough = get_los(filter_cough)
los_tired = get_los(filter_tired)
los_sorethroat = get_los(filter_sorethroat)
los_respiratory = get_los(filter_respiratory)

combine_los = [los_fever, los_cough, los_tired, los_sorethroat, los_respiratory]

plt.boxplot(combine_los)
plt.xticks([1, 2, 3, 4, 5], ['FEVER', 'COUGH', 'TIRED', 'SORETHROAT', 'RESPIRATORY'], fontsize=14)
plt.yticks(fontsize=14)
plt.ylabel('Length of stay', fontsize=20)
plt.title('Length of stay with respect to onset symptoms', fontsize=24)
plt.show()