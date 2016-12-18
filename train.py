# -*- coding:utf-8 -*-

# Kerasのcallbackを試す（modelのsave,restore/TensorBoard書き出し/early stopping）
# @see http://qiita.com/yukiB/items/f45f0f71bc9739830002

# Make data 
import pandas as pd
import numpy as np
import math
import random

def _load_data(data, n_prev = 100):
    """
    data should be pd.DataFrame()
    """

    docX, docY = [], []
    for i in range(len(data)-n_prev):
        docX.append(data.iloc[i:i+n_prev].as_matrix())
        docY.append(data.iloc[i+n_prev].as_matrix())
    alsX = np.array(docX)
    alsY = np.array(docY)

    return alsX, alsY

def train_test_split(df, test_size=0.1, n_prev = 100):
    """
    This just splits data to training and testing parts
    """
    ntrn = round(len(df) * (1 - test_size))
    ntrn = int(ntrn)
    X_train, y_train = _load_data(df.iloc[0:ntrn], n_prev)
    X_test, y_test = _load_data(df.iloc[ntrn:], n_prev)

    return (X_train, y_train), (X_test, y_test)

random.seed(0)
random_factor = 0.05
steps_per_cycle = 80
number_of_cycles = 50
length_of_sequences = 100 # Add

df = pd.DataFrame(np.arange(steps_per_cycle * number_of_cycles + 1), columns=["t"])
df["sin_t"] = df.t.apply(lambda x: math.sin(x * (2 * math.pi / steps_per_cycle)+ random.uniform(-1.0, +1.0) * random_factor))
(X_train, y_train), (X_test, y_test) = train_test_split(df[["sin_t"]], n_prev =length_of_sequences)

# Train model
from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras.layers.recurrent import LSTM
import keras.backend.tensorflow_backend as KTF
import tensorflow as tf
from keras.callbacks import EarlyStopping, TensorBoard, ModelCheckpoint
import os

in_out_neurons = 1
hidden_neurons = 300
#length_of_sequences = 100 # 上へ移動

old_session = KTF.get_session()

with tf.Graph().as_default():
    session = tf.Session('')
    KTF.set_session(session)
    KTF.set_learning_phase(1)
    model = Sequential()  
    with tf.name_scope("inference") as scope:
        model.add(LSTM(hidden_neurons, input_shape=(length_of_sequences, in_out_neurons), return_sequences=False))
        model.add(Dense(in_out_neurons))
        model.add(Activation("linear"))
    model.summary()
    fpath = './tensorlog/weights.{epoch:02d}-{loss:.2f}-{val_loss:.2f}.hdf5'
    cp_cb = ModelCheckpoint(filepath = fpath, monitor='val_loss', verbose=1, save_best_only=True, mode='auto')
    es_cb = EarlyStopping(monitor='val_loss', patience=2, verbose=1, mode='auto')
    tb_cb = TensorBoard(log_dir="./tensorlog", histogram_freq=1)
    model.compile(loss="mean_squared_error", optimizer="rmsprop",  metrics=['accuracy'])
    model.fit(X_train, y_train, batch_size=600, nb_epoch=10, validation_split=0.05, verbose=1, callbacks=[cp_cb, es_cb, tb_cb])
json_string = model.to_json()
#open(os.path.join(f_model,'./tensorlog/rnn_model.json'), 'w').write(json_string)
open(os.path.join('./tensorlog/rnn_model.json'), 'w').write(json_string)
KTF.set_session(old_session)
