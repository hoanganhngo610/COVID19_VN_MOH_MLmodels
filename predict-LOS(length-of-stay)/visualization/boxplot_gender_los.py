import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

path = path = 'df_train.csv'
data = pd.read_csv(path)

filter_male = data.loc[data['SEX'] == 1]
filter_female = data.loc[data['SEX'] == 0]

def get_los(filter_sex):
    los = filter_sex.iloc[:, 17:].values
    return np.reshape(los, len(los)).tolist()

los_male = get_los(filter_male)
los_female = get_los(filter_female)
combine_los = [los_male, los_female]

plt.boxplot(combine_los)
plt.xticks([1, 2], ['Male', 'Female'], fontsize=14)
plt.yticks(fontsize=14)
plt.ylabel('Length of stay', fontsize=20)
plt.title('Length of stay with respect to gender', fontsize=24)
plt.show()