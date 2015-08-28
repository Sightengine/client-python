# -*- coding: utf-8 -*-

from sightengine import client

# Once you create an account on sightengine.com, you will get your own API user and API secret values
# Please do not forget to replace them here
sightengine_client = client.SightengineClient("YOUR_API_USER", "YOUR_API_SECRET")

# Call the Sightengine servers to check for nudity. You can either pass a public URL or a local path. This call will raise an HTTPError if the HTTP connection fails
output = sightengine_client.check_nudity("http://img09.deviantart.net/2bd0/i/2009/276/c/9/magic_forrest_wallpaper_by_goergen.jpg")

print output
