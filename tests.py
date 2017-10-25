import unittest, os
from sightengine.client import SightengineClient

class Tests(unittest.TestCase):
    def test_nudityModel(self):
        client = SightengineClient('1234', 'test')
        checkNudity = client.check('nudity')

        image = os.path.join(os.path.dirname(__file__), 'assets', 'image.jpg')

        output = checkNudity.set_url('https://sightengine.com/assets/img/examples/example5.jpg')
        self.assertEqual('success', output['status'])

        output2 = checkNudity.set_file(image)
        self.assertEqual('success', output2['status'])

        with open(image, mode='rb') as img:
            binary_image = img.read()

        output3 = checkNudity.set_bytes(binary_image)
        self.assertEqual('success', output3['status'])

    def test_allModel(self):
        client = SightengineClient('1234', 'test')
        checkAll = client.check('nudity','wad','properties','type','faces','celebrities')

        image = os.path.join(os.path.dirname(__file__), 'assets', 'image.jpg')

        output = checkAll.set_url('https://sightengine.com/assets/img/examples/example5.jpg')
        self.assertEqual('success', output['status'])

        output2 = checkAll.set_file(image)
        self.assertEqual('success', output2['status'])

        with open(image, mode='rb') as img:
            binary_image = img.read()

        output3 = checkAll.set_bytes(binary_image)
        self.assertEqual('success', output3['status'])

    def test_feedback(self):
        client = SightengineClient('1234', 'test')

        feedback1 = client.feedback('nudity', 'raw', 'https://sightengine.com/assets/img/examples/example5.jpg')
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

    def test_video(self):
        client = SightengineClient('1234', 'test')

        check = client.check('nudity','wad','properties','type','faces','celebrities')
        video_output = check.video('https://sightengine.com/assets/stream/examples/funfair.mp4', 'http://requestb.in/1nm1vw11')
        self.assertEqual('success', video_output['status'])

if __name__ == '__main__':
    unittest.main()