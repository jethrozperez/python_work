### Use Beautiful soup to read in data from a webpage
### Then find the tag, extract the figure and sum across all lines

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter - ')
html = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_314007.html', context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

lst = list()
count = 0

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    x = re.findall('span class="comments">([0-9]+)', tag.decode())
    if len(x) > 0:
        lst = lst + x
        count += 1

y = 0

for item in lst:
    item = int(item)
    y = item + y

print('total is:', y,'\n count is:', count)
