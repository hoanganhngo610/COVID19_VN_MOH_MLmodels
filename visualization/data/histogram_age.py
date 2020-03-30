import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

path = './predict-LOS(length-of-stay)/assets/processed/df_total.csv'
data = pd.read_csv(path)

age = data.iloc[:, 1:2].values
age = np.reshape(age, len(age))

sns.distplot(age, hist=True, kde=True, bins=7, color='darkblue', hist_kws={'edgecolor':'black'}, kde_kws={'linewidth': 3})
plt.title('Distribution of age', fontsize=20)
plt.xlabel('Age', fontsize=14)
plt.show()