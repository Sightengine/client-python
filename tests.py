import unittest, os
from sightengine.client import SightengineClient

class Tests(unittest.TestCase):
    def test_nudityModel(self):
        client = SightengineClient('1234', 'test')
        checkNudity = client.check('nudity')

        output = checkNudity.image('https://sightengine.com/assets/img/examples/example5.jpg')
        self.assertEqual('success', output['status'])

        image = os.path.join(os.path.dirname(__file__), 'assets', 'image.jpg')

        output2 = checkNudity.image(image)
        self.assertEqual('success', output2['status'])

    def test_allModel(self):
        client = SightengineClient('1234', 'test')
        checkNudity = client.check('nudity','wad','properties','type','face')

        output = checkNudity.image('https://sightengine.com/assets/img/examples/example5.jpg')
        self.assertEqual('success', output['status'])


        image = os.path.join(os.path.dirname(__file__), 'assets', 'image.jpg')

        output2 = checkNudity.image(image)
        self.assertEqual('success', output2['status'])

    def test_feedback(self):
        client = SightengineClient('1234', 'test')

        feedback1 = client.feedback('nudity', 'raw', 'https://d3m9459r9kwism.cloudfront.net/img/examples/example5.jpg')
        self.assertEqual('success', feedback1['status'])

        image = os.path.join(os.path.dirname(__file__), 'assets', 'image.jpg')
        feedback2 = client.feedback('nudity', 'safe', image)
        self.assertEqual('success', feedback2['status'])

        feedback3 = client.feedback('model9999', 'raw', 'https://sightengine.com/assets/img/examples/example5.jpg')
        self.assertEqual('failure', feedback3['status'])
        self.assertEqual('argument_error', feedback3['error']['type'])

        feedback4 = client.feedback('nudity', 'raw9999','https://sightengine.com/assets/img/examples/example5.jpg')
        self.assertEqual('failure', feedback4['status'])
        self.assertEqual('argument_error', feedback4['error']['type'])

if __name__ == '__main__':
    unittest.main()