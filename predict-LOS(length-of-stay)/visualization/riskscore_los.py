import numpy as np
import pandas as pd 
from matplotlib import pyplot as plt 

path = 'df_train.csv'
data = pd.read_csv(path)

los = data.iloc[:, 17:].values
risk_score = data.iloc[:, 16:17].values

los = np.reshape(los, len(los)).tolist()
risk_score = np.reshape(risk_score, len(risk_score)).tolist()

plt.scatter(risk_score, los, s=200)
plt.xlabel('Risk score', fontsize=20)
plt.ylabel('Length of stay', fontsize=20)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.title('Length of stay with respect to on risk score', fontsize=24)
plt.show()