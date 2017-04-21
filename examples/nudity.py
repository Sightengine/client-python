from sightengine.client import SightengineClient

client = SightengineClient('API user', 'API secret')

##### feedback

feedback1 = client.feedback('nudity', 'raw', 'https://d3m9459r9kwism.cloudfront.net/img/examples/example5.jpg')
feedback2 = client.feedback('nudity','safe', '/path/to/local/file.jpg')

print(feedback1)
print(feedback2)

####### check image

checkNudity = client.check('nudity')

output = checkNudity.image('/path/to/local/file.jpg')
output2 = checkNudity.image('https://d3m9459r9kwism.cloudfront.net/img/examples/example5.jpg')

print(output)
print(output2)

####### check video

checkNudity = client.check('nudity')
checkNudity.video('http://www.quirksmode.org/html5/videos/big_buck_bunny.webm', 'http://requestb.in/1nm1vw11')