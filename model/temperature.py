# -*- coding:utf-8 -*-

from keras.models import Sequential, model_from_json
from keras.layers.core import Dense, Activation
from keras.layers.recurrent import LSTM
import numpy as np
import os
import time

class Temperature(object):
    OUTPUT_DIM = 32 #内部の射影と最終的な出力の次元
    MODEL_FILE = os.path.join('model', 'model.json')
    WEIGHTS_FILE = os.path.join('model', 'weights.hdf5')
    DT_FORMAT = '%H:%M:%S'

    def __init__(self):
        self.model = None
        
    def train(self, X, y, dev=False):
        """モデルの学習を行い、その結果を保存する
        @param X: 学習データ(予測に使われるパラメータ＝月,日)
        @param y: 学習データ(予測したい値＝平均気温)
        """
        if dev and os.path.exists(Temperature.MODEL_FILE):
            model_json = open(Temperature.MODEL_FILE).read()
            print 'Load model from', Temperature.MODEL_FILE
            self.model = model_from_json(model_json)
        else:
            self.model = Sequential([
                LSTM(Temperature.OUTPUT_DIM, input_shape=X.shape),
                Dense(1),
                Activation('linear')
            ])
            self.model.compile(loss='mean_squared_error', optimizer='rmsprop')
            model_json = self.model.to_json()
            print 'model_json:', model_json #DEBUG
            print 'Save model to', Temperature.MODEL_FILE, 'at', time.strftime(Temperature.DT_FORMAT)
            with open(Temperature.MODEL_FILE, 'w') as f:
                f.write(model_json)
                f.close()
        
        print 'Train started at', time.strftime(Temperature.DT_FORMAT)
        self.model.fit(X, y, batch_size=128, validation_split=0.05)
        print 'Train finished at', time.strftime(Temperature.DT_FORMAT)
        
        print 'Save weights to', Temperature.WEIGHTS_FILE
        self.model.save_weights(Temperature.WEIGHTS_FILE)

    def load(self):
        """学習済みモデルを読み込む
        """
        assert os.path.exists(Temperature.MODEL_FILE)
        assert os.path.exists(Temperature.WEIGHTS_FILE)
        
        model_json = open(Temperature.MODEL_FILE).read()
        print 'Load model from', Temperature.MODEL_FILE
        self.model = model_from_json(model_json)
        
        print 'Load weights from', Temperature.WEIGHTS_FILE
        self.model.load_weights(Temperature.WEIGHTS_FILE)

    def predict(self, month, day):
        """モデルを使って平均気温を予測する
        @param month: 月
        @param day: 日
        """
        assert self.model is not None
        
        X = np.array([[month, day]])
        print 'X:', X #DEBUG
        predicted = self.model.predict(X)
        print 'predicted:', predicted
        return predicted
