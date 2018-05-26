import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter location: ')

print(url)

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
tree = ET.fromstring(data)
sum1 = int(0)

count = tree.findall('comments/comment')
for item in count:
    x = int(item.find('count').text)
    sum1 = x + sum1

print('Count: ', len(count))
print('Sum: ', sum1)


