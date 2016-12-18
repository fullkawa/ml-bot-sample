# ml-bot-sample

機械学習を使ったボットのサンプルプログラム

## バージョン情報

* Python 2.7
* Tensorflow 0.10.0rc0
* Keras 1.1.2
* python-rtmbot 0.4.0

## 概要

yukiB氏の
[Kerasのcallbackを試す（modelのsave,restore/TensorBoard書き出し/early stopping）](http://qiita.com/yukiB/items/f45f0f71bc9739830002)
を利用し、RNN(LSTM)にsin波を学習させ、その値を返すボットという設定です。

## 使い方

### インストール

バージョン情報に記載のパッケージがインストールされていない場合はそれをインストールします。
Tensorflowは`pip install tensorflow`, Kerasは`pip install keras`, python-rtmbotは`pip install rtmbot`でインストールできます。

### モデルにsin波を学習させる

`git clone https://github.com/fullkawa/ml-bot-sample.git`でソースコードをチェックアウトした後、`python train.py`

```
112-233:ml-bot-sample y.furukawa$ python train.py
Using TensorFlow backend.
____________________________________________________________________________________________________
Layer (type)                     Output Shape          Param #     Connected to
====================================================================================================
lstm_1 (LSTM)                    (None, 300)           362400      lstm_input_1[0][0]
____________________________________________________________________________________________________

dense_1 (Dense)                  (None, 1)             301         lstm_1[0][0]
____________________________________________________________________________________________________
activation_1 (Activation)        (None, 1)             0           dense_1[0][0]
====================================================================================================
Total params: 362701
____________________________________________________________________________________________________
Train on 3325 samples, validate on 176 samples
Epoch 1/10
3000/3325 [==========================>...] - ETA: 4s - loss: 0.2627 - acc: 0.0000e+00 Epoch 00000: val_loss improved from inf to 0.19250, saving model to ./tensorlog/weights.00-0.24-0.19.hdf5
3325/3325 [==============================] - 49s - loss: 0.2408 - acc: 3.0075e-04 - val_loss: 0.1925 - val_acc: 0.0000e+00
Epoch 2/10
3000/3325 [==========================>...] - ETA: 4s - loss: 0.0456 - acc: 3.3333e-04 Epoch 00001: val_loss improved from 0.19250 to 0.00085, saving model to ./tensorlog/weights.01-0.04-0.00.hdf5
3325/3325 [==============================] - 48s - loss: 0.0412 - acc: 3.0075e-04 - val_loss: 8.4748e-04 - val_acc: 0.0000e+00
Epoch 3/10
3000/3325 [==========================>...] - ETA: 4s - loss: 0.0015 - acc: 3.3333e-04     Epoch 00002: val_loss did not improve
3325/3325 [==============================] - 47s - loss: 0.0024 - acc: 3.0075e-04 - val_loss: 0.0228 - val_acc: 0.0000e+00
Epoch 4/10
3000/3325 [==========================>...] - ETA: 4s - loss: 0.0189 - acc: 3.3333e-04 Epoch 00003: val_loss did not improve
3325/3325 [==============================] - 46s - loss: 0.0177 - acc: 3.0075e-04 - val_loss: 0.0055 - val_acc: 0.0000e+00
Epoch 5/10
3000/3325 [==========================>...] - ETA: 4s - loss: 0.0089 - acc: 3.3333e-04 Epoch 00004: val_loss did not improve
3325/3325 [==============================] - 47s - loss: 0.0095 - acc: 3.0075e-04 - val_loss: 0.0163 - val_acc: 0.0000e+00
Epoch 00004: early stopping
```

上記"rnn_model.json"がモデルデータ、"weights.*.hdf5"が学習済みパラメータデータとなります。

### Slackのトークンを取得する

"rtmbot.conf_sample"を"rtmbot.conf"にリネームします。  
次に[新しいBotUserを作成](https://api.slack.com/bot-users)し、そのトークンを"rtmbot.conf"のSLACK_TOKENに記載します。  

### ボットを実行する

`rtmbot`

Slackにボットを追加し、`@[ボット名] [整数]`とメッセージを送ります。
