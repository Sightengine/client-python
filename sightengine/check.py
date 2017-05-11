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

VERSION = None
path_version = os.path.join(os.path.dirname(__file__), '../version.py')
exec(open(path_version).read())

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
        self.endpoint = 'https://api.sightengine.com/'
        self.modelsType = ''

        if len(args) > 1:
            for arg in args:
                print(arg)
                self.modelsType += arg + ','
            self.modelsType = self.modelsType[:-1]
        else:
            self.modelsType = args[0]

    def image(self, image):
        numberOfModels = self.modelsType.count(",")

        if numberOfModels > 0:
            if image.lower().startswith(('http://', 'https://')):
                url = self.endpoint + '1.0/check.json'
                r = requests.get(url, params={'models': self.modelsType, 'url': image, 'api_user': self.api_user, 'api_secret': self.api_secret},  headers=headers)
            else:
                url = self.endpoint + '1.0/check.json'
                r = requests.post(url, files={'media': open(image, 'rb')}, data={'models': self.modelsType,'api_user': self.api_user, 'api_secret': self.api_secret},  headers=headers)

            output = json.loads(r.text)
            return output
        else:
            if image.lower().startswith(('http://', 'https://')):
                url = self.endpoint + '1.0' + '/' + self.modelsType + '.json'
                r = requests.get(url, params={'url': image, 'api_user': self.api_user, 'api_secret': self.api_secret},  headers=headers)
            else:
                url = self.endpoint + '1.0' + '/' + self.modelsType + '.json'
                r = requests.post(url, files={'media': open(image, 'rb')}, data={'api_user': self.api_user,'api_secret': self.api_secret},  headers=headers)

            output = json.loads(r.text)
            return output

    def video(self, videoUrl, callbackUrl):
        url =  self.endpoint + '1.0/video/moderation.json?stream_url=' + videoUrl + '&callback_url=' + callbackUrl + '&api_user=' + self.api_user + '&api_secret=' + self.api_secret
        r = requests.get(url,  headers=headers)

        output = json.loads(r.text)
        return output







