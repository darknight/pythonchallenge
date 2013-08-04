import re
import urllib2

next_id = re.compile(r'and the next nothing is (\d+)')
cur_id = 12345
prefix = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s'

for i in range(400):
    url = prefix % cur_id
    fp = urllib2.urlopen(url, timeout=60)
    page = fp.read()
    res = next_id.search(page)
    if res is None:
        if 'Divide' in page:
            cur_id = int(cur_id) / 2
        else:
            print page
            break
    else:
        cur_id = res.group(1)
