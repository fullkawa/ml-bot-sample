# -*- coding:utf-8 -*-

import pandas as pd
from model.temperature import Temperature

DATA_FILE = 'data.csv'

data = pd.DataFrame.from_csv(DATA_FILE, header=3)
print data.head()
