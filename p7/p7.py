import Image

def main():
    im = Image.open('oxygen.png')
    width, height = im.size
    box = (0, height / 2, width, height / 2 + 1)
    region = im.crop(box)
    data = region.getdata()
    word = []
    for d in data:
        r, g, b, a = d
        word.append(chr(r))
    print 'word is'
    print ''.join(word)

if __name__ == '__main__':
    main()
    # get hint from main(), the printed result is not very elegant
    # TODO: need rewriting
    hint = (105, 110, 116, 101, 103, 114, 105, 116, 121,)
    print ''.join(map(chr, hint))
