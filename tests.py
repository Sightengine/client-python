import unittest, os
from sightengine.client import SightengineClient

class Tests(unittest.TestCase):
    def test_nudityModel(self):
        client = SightengineClient('test', 'test')
        checkNudity = client.check('nudity')

        output = checkNudity.image('https://d3m9459r9kwism.cloudfront.net/img/examples/example5.jpg')
        self.assertEqual('success', output['status'])

        output2 = checkNudity.image('https://incorrectUrl.jpg')
        self.assertEqual('failure', output2['status'])
        self.assertEqual('media_error', output2['error']['type'])

        image = os.path.join(os.path.dirname(__file__), 'assets', 'image.jpg')

        output3 = checkNudity.image(image)
        self.assertEqual('success', output3['status'])

    def test_allModel(self):
        client = SightengineClient('test', 'test')
        checkNudity = client.check('nudity','wad','properties','type','face')

        output = checkNudity.image('https://d3m9459r9kwism.cloudfront.net/img/examples/example5.jpg')
        self.assertEqual('success', output['status'])

        output2 = checkNudity.image('https://incorrectUrl.jpg')
        self.assertEqual('failure', output2['status'])
        self.assertEqual('media_error', output2['error']['type'])

        image = os.path.join(os.path.dirname(__file__), 'assets', 'image.jpg')

        output3 = checkNudity.image(image)
        self.assertEqual('success', output3['status'])

    def test_feedback(self):
        client = SightengineClient('test', 'test')

        feedback1 = client.feedback('nudity', 'raw', 'https://d3m9459r9kwism.cloudfront.net/img/examples/example5.jpg')
        self.assertEqual('success', feedback1['status'])

        image = os.path.join(os.path.dirname(__file__), 'assets', 'image.jpg')
        feedback2 = client.feedback('nudity', 'safe', image)
        self.assertEqual('success', feedback2['status'])

        feedback3 = client.feedback('nudity', 'raw', 'https://incorrectUrl.jpg')
        self.assertEqual('failure', feedback3['status'])
        self.assertEqual('media_error', feedback3['error']['type'])

        feedback4 = client.feedback('model9999', 'raw', 'https://d3m9459r9kwism.cloudfront.net/img/examples/example5.jpg')
        self.assertEqual('failure', feedback4['status'])
        self.assertEqual('argument_error', feedback4['error']['type'])

if __name__ == '__main__':
    unittest.main()