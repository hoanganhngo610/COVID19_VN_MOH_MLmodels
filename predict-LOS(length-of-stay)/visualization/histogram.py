import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

path = 'df_total.csv'
data = pd.read_csv(path)

age = data.iloc[:, 1:2].values
age = np.reshape(age, len(age))

doo = data.iloc[:, 8:9].values
doo = np.reshape(doo, len(doo))

plt.subplot(2,1,1)
sns.distplot(doo, hist=True, kde=True, bins=6, color='darkblue', hist_kws={'edgecolor':'black'}, kde_kws={'linewidth': 3})
plt.title('Day of onset')

plt.subplot(2,1,2)
sns.distplot(age, hist=True, kde=True, bins=7, color='darkblue', hist_kws={'edgecolor':'black'}, kde_kws={'linewidth': 3})
plt.title('Distribution of age')

plt.show()