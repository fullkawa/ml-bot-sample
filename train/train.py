# -*- coding:utf-8 -*-

# Usage: ml-bot-sample you$ python train/train.py
import sys
sys.path.append('.')

import os
import pandas as pd
import matplotlib.pyplot as plt
import time
from model.temperature import Temperature

DATA_FILE = os.path.join('train', 'data.csv')
DT_FORMAT = '%H:%M:%S'

data = pd.DataFrame.from_csv(DATA_FILE, header=2, index_col=None, parse_dates=False)
print '\n[data]'
print data.head()

X_train = data.iloc[:730, 1:3] #DEV
print '\n[train data: X]', X_train.shape
print X_train.head()

y_train = data.iloc[:730, 3] #DEV
print '\n[train data: y]', y_train.shape
print y_train.head()

temp = Temperature()
print '\n*** train start at', time.strftime(DT_FORMAT)
temp.train(X_train.values, y_train.values, dev=True)
print '\n*** train finished at', time.strftime(DT_FORMAT)
