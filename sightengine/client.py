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

import requests, json, os
import sightengine
from .check import Check

VERSION = sightengine.__version__

headers = requests.utils.default_headers()
headers.update(
    {
        'User-Agent': 'SE-SDK-Python ' + VERSION,
    }
)

class SightengineClient(object):
    modelVersions = {}

    def __init__(self, api_user, api_secret):
        self.api_user = api_user
        self.api_secret = api_secret
        self.endpoint = 'https://api.sightengine.com/'

    def feedback(self, model, modelClass, image):
        if not model:
            raise Exception('Please provide the version of the model ' + model)

        if image.lower().startswith(('http://', 'https://')):
            url = self.endpoint + '1.0/feedback.json'
            r = requests.get(url, params={'model': model, 'class': modelClass, 'url': image, 'api_user': self.api_user, 'api_secret': self.api_secret}, headers=headers)
        else:
            url =  self.endpoint + '1.0/feedback.json'
            r = requests.post(url, files={'media': open(image, 'rb')}, data={'model': model, 'class': modelClass, 'api_user': self.api_user, 'api_secret': self.api_secret}, headers=headers)

        output = json.loads(r.text)
        return output

    def check(self, *args):
        return Check(self.api_user,self.api_secret, *args)

