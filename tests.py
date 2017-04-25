import unittest
from sightengine.client import SightengineClient

class Tests(unittest.TestCase):
    def test_nudity(self):
        client = SightengineClient('test', 'test')
        checkNudity = client.check('nudity')

        output = checkNudity.image('https://d3m9459r9kwism.cloudfront.net/img/examples/example5.jpg')

        self.assertEqual('success', output['status'])

        output2 = checkNudity.image('https://incorrectUrl.jpg')

        self.assertEqual('failure', output2['status'])
        self.assertEqual('media_error', output2['error']['type'])


if __name__ == '__main__':
    unittest.main()