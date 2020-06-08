import json
import urllib.request
import urllib.parse
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_641773.json"
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
info = json.loads(data)
print('User count:', len(info))
sum = 0
for item in info['comments']:
    sum += int(item['count'])
print(sum)
