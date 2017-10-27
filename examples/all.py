from sightengine.client import SightengineClient

client = SightengineClient('API user', 'API secret')

####### check image

checkAll = client.check('nudity', 'wad', 'properties', 'faces', 'type')

output = checkAll.set_file('/path/to/local/file.jpg')
output2 = checkAll.set_url('https://d3m9459r9kwism.cloudfront.net/img/examples/example7.jpg')

# assign binary_image
output3 = checkAll.set_bytes(binary_image)

print(output)
print(output2)
print(output3)
