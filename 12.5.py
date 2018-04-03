import urllib.request, urllib.parse, urllib.error, time
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count = int(input('Count: '))
position = int(input('Position: '))
inc_count = int(1)
inc_position = int(1)

while inc_count <= count:

    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')

    for tag in tags:
        if inc_position == position:
            url = tag.get('href', None)
            newurlname = tag.contents[0]
            print(url)
            break
        else:
            inc_position = inc_position + 1
            continue

    inc_position = int(1)
    inc_count = inc_count + 1
