Sightengine Python Client
===============

Nudity detection and moderation - Python library to connect to the Sightengine API

About
-----

Use the Sightengine nudity API to instantly moderate adult content in user-submitted photos. See http://sightengine.com for more information.


Instructions
------

1. Create an account on http://sightengine.com, you will get your own API_USER and API_SECRET values
2. Import the Sightengine package
3. Create a SightengineClient object and use it as shown in the example


Examples
--------

Moderate an image accessible through a public URL:

  from sightengine import client
  sightengine_client = client.SightengineClient("YOUR_API_USER", "YOUR_API_SECRET")
  output = sightengine_client.check_nudity("http://img09.deviantart.net/2bd0/i/2009/276/c/9/magic_forrest_wallpaper_by_goergen.jpg")
  print output


Moderate a local image:

  from sightengine import client
  sightengine_client = client.SightengineClient("YOUR_API_USER", "YOUR_API_SECRET")
  output = sightengine_client.check_nudity("/full/path/to/image.jpg")
  print output
