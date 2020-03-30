import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

path = './predict-LOS(length-of-stay)/assets/processed/df_total.csv'

data = pd.read_csv(path, usecols=[6])

doo = data.values
doo = np.reshape(doo, len(doo))

sns.distplot(doo, hist=True, kde=True, bins=6, color='darkblue', hist_kws={'edgecolor':'black'}, kde_kws={'linewidth': 3})
plt.title('Days', fontsize=20)
plt.xlabel('Days of onset', fontsize=14)
plt.show()