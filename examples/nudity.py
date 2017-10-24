from sightengine.client import SightengineClient

client = SightengineClient('API user', 'API secret')

##### feedback

feedback1 = client.feedback('nudity', 'raw', 'https://d3m9459r9kwism.cloudfront.net/img/examples/example5.jpg')
feedback2 = client.feedback('nudity','safe', '/path/to/local/file.jpg')

print(feedback1)
print(feedback2)

####### check image

checkNudity = client.check('nudity')

output = checkNudity.set_file('/path/to/local/file.jpg')
output2 = checkNudity.set_url('https://d3m9459r9kwism.cloudfront.net/img/examples/example5.jpg')

# assign binary_image
output3 = checkNudity.set_bytes(binary_image)

print(output)
print(output2)
print(output3)

####### check video

check = client.check('nudity', 'wad')
output = check.video('http://www.quirksmode.org/html5/videos/big_buck_bunny.webm', 'http://requestb.in/1nm1vw11')

print(output)