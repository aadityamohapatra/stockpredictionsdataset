import os
import pandas as pd
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
    if int(df['Date'][i][:4]) < 2015:
        df = df.drop([i])
    else:
        break
df = df.reset_index(drop=True)



rolling = pd.DataFrame({'Date': [], 'Open': [], 'High': [], 'Low': [],
                        'Close': [], 'Adj close' : [], 'Volume': []})


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
        #breakpoint()
        rolling = rolling.append(final, ignore_index = True)
        month = df.Date.iloc[i][5:7]
        days = 0

print(rolling)
