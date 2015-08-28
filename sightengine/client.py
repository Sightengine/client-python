# -*- coding: utf-8 -*-
"""
Copyright (c) 2015 Sightengine
http://www.sightengine.com/
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

import requests
import json

class SightengineClient(object):

    def __init__(self, api_user, api_secret):
        """
        Sightengine Client initialization
        """
        self._api_user = api_user
        self._api_secret = api_secret

    @property
    def api_user(self):
        return self._api_user

    @property
    def api_secret(self):
        return self._api_secret

    def check_nudity(self, image):
        endpoint = 'http://api.sightengine.com'
        version = '1.0'
        url = endpoint+'/'+version+'/nudity.json'

        if image[:7].lower()=='http://' or image[:8].lower()=='https://':
            r = requests.post(url, data={'url':image, 'api_user':self._api_user, 'api_secret':self._api_secret})
        else:
            r = requests.post(url, files={'photo': open(image, 'rb')}, data={'api_user':self._api_user, 'api_secret':self._api_secret})

        r.raise_for_status()

        output = json.loads(r.text)

        return output
