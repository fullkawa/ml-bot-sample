# -*- coding:utf-8 -*-

from __future__ import print_function
from __future__ import unicode_literals

from rtmbot.core import Plugin
import re

class SinPlugin(Plugin):

    def process_message(self, data):
        print('data:', data) #DEBUG
        text = data[u'text'].encode('utf-8')
        r = re.compile(r'<@.+> (.+)')
        match = r.search(text)
        print('match(1):', match.group(1)) #DEBUG
        if match and match.group(1):
            try:
                in_value = int(match.group(1))
                print('in_value:', in_value) #DEBUG
                message = [data[u'channel'], str(in_value)]
            except ValueError:
                message = [data[u'channel'], '整数を入力してください']
            self.outputs.append(message)
