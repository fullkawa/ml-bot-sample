# ml-bot-sample

機械学習を使ったボットのサンプルプログラム

## バージョン情報

* Python 2.7
* Tensorflow 0.10.0rc0
* Keras 0.3.0

## 概要

yukiB氏の
[Kerasのcallbackを試す（modelのsave,restore/TensorBoard書き出し/early stopping）](http://qiita.com/yukiB/items/f45f0f71bc9739830002)
を利用し、RNN(LSTM)にsin波を学習させ、その値を返すボットという設定です。

## 使い方

### モデルにsin波を学習させる

`git clone https://github.com/fullkawa/ml-bot-sample.git`でソースコードをチェックアウトした後、`python train.py`

```
112-233:ml-bot-sample y.furukawa$ python train.py
Using TensorFlow backend.
Train on 3325 samples, validate on 176 samples
Epoch 1/10
3325/3325 [==============================] - 27s - loss: 0.2050 - val_loss: 0.1024
Epoch 00000: val_loss improved from inf to 0.10237, saving model to ./weights.00.hdf5
Epoch 2/10
3325/3325 [==============================] - 25s - loss: 0.0341 - val_loss: 0.0009
Epoch 00001: val_loss improved from 0.10237 to 0.00093, saving model to ./weights.01.hdf5
Epoch 3/10
3325/3325 [==============================] - 26s - loss: 0.0009 - val_loss: 0.0009
Epoch 00002: val_loss improved from 0.00093 to 0.00091, saving model to ./weights.02.hdf5
Epoch 4/10
3325/3325 [==============================] - 25s - loss: 0.0028 - val_loss: 0.0301
Epoch 00003: val_loss did not improve
Epoch 5/10
3325/3325 [==============================] - 25s - loss: 0.0200 - val_loss: 0.0045
Epoch 00004: val_loss did not improve
Epoch 6/10
3325/3325 [==============================] - 25s - loss: 0.0033 - val_loss: 0.0068
Epoch 00005: val_loss did not improve
Epoch 00005: early stopping
112-233:ml-bot-sample y.furukawa$
112-233:ml-bot-sample y.furukawa$ ls -al
 (中略)
-rw-r--r--   1 y.furukawa  222086365      829 12 18 17:55 rnn_model.json
-rw-r--r--   1 y.furukawa  222086365     3687 12 18 17:52 train.py
-rw-r--r--   1 y.furukawa  222086365  1460448 12 18 17:53 weights.00.hdf5
-rw-r--r--   1 y.furukawa  222086365  1460448 12 18 17:54 weights.01.hdf5
-rw-r--r--   1 y.furukawa  222086365  1460448 12 18 17:54 weights.02.hdf5
```

上記"rnn_model.json"がモデルデータ、"weights.*.hdf5"が学習済みパラメータデータとなります。


