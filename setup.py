from setuptools import setup
import os

VERSION = None
path_version = os.path.join(os.path.dirname(__file__), '../version.py')
exec(open(path_version).read())

setup(
  name = 'sightengine',
  packages = ['sightengine'],
  version = VERSION,
  description = 'Sightengine Python client',
  author = 'Sightengine',
  author_email='support@sightengine.com',
  url = 'https://github.com/Sightengine/client-python'
)