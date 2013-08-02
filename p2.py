import urllib2
import re
from collections import defaultdict

extr = re.compile(r'<!--\s*(.*)\s*-->\s*<!--\s*([\s|\S]*)\s*-->')
url = 'http://www.pythonchallenge.com/pc/def/ocr.html'

fp = urllib2.urlopen(url, timeout=60)
page = fp.read()
res = extr.search(page)
data = res.group(2)

d = defaultdict(int)
for letter in data:
    d[letter] += 1
l = list(d.items())
l.sort(key=lambda x: x[1])
print l
