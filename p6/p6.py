import re

next_hint = re.compile(r'[A-Za-z\s]+(\d+)')
next_file = 90052

def find_next():
    while True:
        fname = str(next_file) + '.txt'
        with open(fname) as f:
            line = f.readline()
            res = next_hint.search(line)
            if res:
                next_file = res.group(1)
            else:
                print fname
                print line
                break
