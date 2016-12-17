# -*- coding:utf-8 -*-

from keras.models import Sequential
from keras.layers import Dense, Activation
from numpy as np

class Temperature(object):
    OUTPUT_DIM = 32 #内部の射影と最終的な出力の次元
    WEIGHTS_FILE = 'weights.hdf5'

    def __init__(self):
        self.model = Sequential([
            LSTM(OUTPUT_DIM),
            Dense(1),
            Activation('linear')
        ])
        self.model.compile(loss='mean_squared_error', optimizer='rmsprop')

    def train(self, X, y, batch_size):
        """モデルの学習を行い、その結果を保存する
        @param X: 学習データ(予測に使われるパラメータ＝月,日)
        @param y: 学習データ(予測したい値＝平均気温)
        @param batch_size: 学習データのサイズ
        """
        self.model.fit(X, y, batch_size=batch_size, validation_split=0.05)
        self.model.save_weights(WEIGHTS_FILE)

    def load(self):
        """学習済みモデルを読み込む
        """
        self.model.load_weights(WEIGHTS_FILE)

    def predict(self, month, day):
        X = np.array([[month, day]])
        print 'X:', X #DEBUG
        predicted = self.model.predict(X)
        print 'predicted:', predicted
        return predicted
