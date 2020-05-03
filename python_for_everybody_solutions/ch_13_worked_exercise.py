### Ch 13 Ex 1

## Create a program that will promp to input a URL, read the XML data from that URL using
### using urlib and then parse and extract the comment counts from the XML data and compute the sum in the file

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

##site = Input('Enter URL: ')

site = ' http://py4e-data.dr-chuck.net/comments_314009.xml'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

fhand = urllib.request.urlopen(site, context=ctx).read()


tree = ET.fromstring(fhand)

comment_lst = tree.findall('comments/comment')


total = 0

for comment in comment_lst:
     x = int(comment.find('count').text)
     total = total + x

print(total)
