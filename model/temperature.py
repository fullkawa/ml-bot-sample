# -*- coding:utf-8 -*-

from keras.models import Sequential
from keras.layers import Dense, Activation

class Temperature(object):
    def __init__(self):
        self.model = Sequential([
            Dense(32, input_dim=2),
            Activation('linear'),
        ])
