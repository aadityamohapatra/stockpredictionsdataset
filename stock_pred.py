import os
import pandas as pd
from pandasgui import show
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import *
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


path = "C:/Users/Jesus/Documents/GitHub/stockpredictionsdataset/stocks/"
filenames = []
for fname in os.listdir(path):
    filenames.append(fname)


df = pd.read_csv('{}{}'.format(path, filenames[0]))

for i in range(df.shape[0] - 1):
    if int(df['Date'][i][:4]) < 2014:
        df = df.drop([i])
    else:
        break
df = df.reset_index(drop=True)



rolling = pd.DataFrame({'Date': [], 'Open': [], 'High': [], 'Low': [],
                        'Close': [], 'Adj Close' : [], 'Volume': []})


month = int(df.Date.iloc[0][5:7])
sums = [0, 0, 0, 0, 0, 0]
days = 0
for i in range(df.shape[0]):
    if int(df.Date.iloc[i][5:7]) == month:
        for j in range(6):
            sums[j] += df.iloc[i][j+1]
        days += 1
    else:
        for j in range(6):
            sums[j] = sums[j]/days
        final = {'Date':df.Date.iloc[i-1][:7], 'Open': sums[0], 'High': sums[1],
                'Low': sums[2], 'Close': sums[3], 'Adj Close': sums[4],
                'Volume': sums[5]}

        rolling = rolling.append(final, ignore_index = True)

        month = int(df.Date.iloc[i][5:7])
        days = 1
        for k in range(6):
            sums[k]=df.iloc[i][k+1]

show(rolling, settings={'block': True})
