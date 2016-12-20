# -*- coding:utf-8 -*-

from __future__ import print_function
from __future__ import unicode_literals

import glob
import numpy as np
from rtmbot.core import Plugin
import re

from keras.models import model_from_json

class SinPlugin(Plugin):
    model_json = open('tensorlog/rnn_model.json', 'r').read()
    model = model_from_json(model_json)
    print('Model loaded.')
    
    files = glob.glob('tensorlog/weights.*.hdf5')
    model.load_weights(files[-1])
    print('Weights loaded from', files[-1])
    print('READY!')

    def process_message(self, data):
        text = data[u'text'].encode('utf-8')
        r = re.compile(r'<@(.+)>')
        match = r.search(text)
        if match and match.group(1): # DMのときのみ
            X = np.zeros((1,100,1))
            for i in range(0, 100):
                X[0, i, 0] = i # 本サンプルでは固定とする
            predicted = self.model.predict(X, batch_size=1)
            print('predicted:', predicted) #DEBUG
            message = [data[u'channel'], 'sin={0}'.format(predicted[0][0])]
            self.outputs.append(message)
