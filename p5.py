import urllib2
import pickle
import pprint

url = 'http://www.pythonchallenge.com/pc/def/banner.p'

fp = urllib2.urlopen(url)
page = fp.read()
data = pickle.loads(page)
for li in data:
    line = ''
    for t in li:
        line += t[0] * t[1]
    print line

