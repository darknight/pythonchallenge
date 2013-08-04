import urllib2
import re

comment = re.compile(r'<!--\s*([\s|\S]*)\s*-->')
answer = re.compile(r'[^A-Z]([A-Z]{3}[a-z][A-Z]{3})[^A-Z]')
url = 'http://www.pythonchallenge.com/pc/def/equality.html'

fp = urllib2.urlopen(url)
page = fp.read()
res = comment.search(page)
data = res.group(1)
res = answer.findall(data)
print ''.join([v[3] for v in res])
