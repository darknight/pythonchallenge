import string

keys = string.letters[:26]
values = keys[2:] + keys[:2]
d = dict(zip(keys, values))

data = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
out = ""
for k in data:
    if k in d:
        out = out + d[k]
    else:
        out = out + k
print out

# use string.maketrans() for url
url = 'map.html'
_map = string.maketrans(keys, values)
print url.translate(_map)
