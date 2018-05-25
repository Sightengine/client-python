# -*- coding: utf-8 -*-
"""
Copyright (c) 2017 Sightengine
http://sightengine.com/
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

import requests, json, sightengine
from io import BytesIO

VERSION = sightengine.__version__

headers = requests.utils.default_headers()
headers.update(
    {
        'User-Agent': 'SE-SDK-Python ' + VERSION,
    }
)

class Check(object):
    def __init__(self, api_user, api_secret, *args):
        self.api_user = api_user
        self.api_secret = api_secret
        self.endpoint = 'https://api.sightengine.com/1.0/'
        self.modelsType = ''

        if len(args) > 1:
            for arg in args:
                self.modelsType += arg + ','
            self.modelsType = self.modelsType[:-1]
        else:
            self.modelsType = args[0]

    def set_url(self, imageUrl):
        r = requests.get(self.endpoint + 'check.json', params={'models': self.modelsType, 'url': imageUrl, 'api_user': self.api_user, 'api_secret': self.api_secret}, headers=headers)

        output = json.loads(r.text)
        return output

    def set_file(self, file):
        r = requests.post(self.endpoint + 'check.json', files={'media': open(file, 'rb')}, data={'models': self.modelsType, 'api_user': self.api_user,'api_secret': self.api_secret}, headers=headers)

        output = json.loads(r.text)
        return output

    def set_bytes(self, binaryImage):
        r = requests.post(self.endpoint + 'check.json', files={'media': BytesIO(binaryImage)}, data={'models': self.modelsType, 'api_user': self.api_user, 'api_secret': self.api_secret}, headers=headers)

        output = json.loads(r.text)
        return output

    def video(self, videoUrl, callbackUrl):
        r = requests.get(self.endpoint + 'video/check.json', params={'models': self.modelsType, 'callback_url': callbackUrl, 'stream_url': videoUrl, 'api_user': self.api_user, 'api_secret': self.api_secret}, headers=headers)

        output = json.loads(r.text)
        return output

    def video_sync(self, videoUrl):
        r = requests.get(self.endpoint + 'video/check-sync.json', params={'models': self.modelsType, 'stream_url': videoUrl, 'api_user': self.api_user, 'api_secret': self.api_secret}, headers=headers)

        output = json.loads(r.text)
        return output







