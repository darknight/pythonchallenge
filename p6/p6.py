import re
import os
import sys
import zipfile
import shutil

next_hint = re.compile(r'[A-Za-z\s]+(\d+)')
next_file = 90052

def main(zipobj, dirname):
    global next_file
    comments = []
    while True:
        fname = str(next_file) + '.txt'
        path = dirname + '/' + fname
        with open(path) as f:
            cmt = zipobj.getinfo(fname).comment
            comments.append(cmt)
            line = f.readline()
            res = next_hint.search(line)
            if res:
                next_file = res.group(1)
            else:
                break
    print ''.join(comments)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'provide path of channel.zip'
        sys.exit(1)
    fname = sys.argv[1]
    zipobj = zipfile.ZipFile(fname)
    todir = os.getcwd() + '/tmp'
    zipobj.extractall(path=todir)
    main(zipobj, todir)
    shutil.rmtree(todir)
