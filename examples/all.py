from sightengine.client import SightengineClient

client = SightengineClient('API user', 'API secret')

####### check image

checkAll = client.check('nudity', 'wad', 'properties', 'face', 'type')

output = checkAll.image('/path/to/local/file.jpg')
output2 = checkAll.image('https://d3m9459r9kwism.cloudfront.net/img/examples/example7.jpg')

print(output)
print(output2)
