# All portions of the code written by Andrew Lei are Copyright (c) 2011


#Bruteforce way of climbing through www.bookfinder.com's listing of all
#isbns to compile an isbn list in a file

def isbncomp(url):

    import urllib.request
    import re


    content = urllib.request.urlopen(url).read()

    isbnlink = re.findall(r'(http://www\.bookfinder\.com/dir/[\d\w]*?)/\?ref=bf', str(content))

    f = open('isbnlist.txt','w')

    for link in isbnlink:
        content1 = urllib.request.urlopen(link).read()
        isbnlink2 = re.findall(r'(http://www\.bookfinder\.com/dir/[\d\w]*?)/\?ref=bf', str(content1))

        for link2 in isbnlink2:
            content2 = urllib.request.urlopen(link2).read()
            isbn = re.findall(r'small>\((\d\d\d\d\d\d\d\d\d[\d\w])',str(content2))
            for i in isbn:
                f.write(i + "\n")

    f.close()



isbncomp('http://www.bookfinder.com/dir/e3bb/')
isbncomp('http://www.bookfinder.com/dir/e3bc/')
isbncomp('http://www.bookfinder.com/dir/e3bd/')
isbncomp('http://www.bookfinder.com/dir/e3be/')
isbncomp('http://www.bookfinder.com/dir/e3bf/')
isbncomp('http://www.bookfinder.com/dir/e3c0/')
isbncomp('http://www.bookfinder.com/dir/e3c1/')
isbncomp('http://www.bookfinder.com/dir/e3c2/')
isbncomp('http://www.bookfinder.com/dir/e3c3/')
isbncomp('http://www.bookfinder.com/dir/e3c4/')
isbncomp('http://www.bookfinder.com/dir/e3c5/')
isbncomp('http://www.bookfinder.com/dir/e3c6/')
isbncomp('http://www.bookfinder.com/dir/e3c7/')
isbncomp('http://www.bookfinder.com/dir/e3c8/')
isbncomp('http://www.bookfinder.com/dir/e3c9/')
isbncomp('http://www.bookfinder.com/dir/e3ca/')
isbncomp('http://www.bookfinder.com/dir/e3cb/')
isbncomp('http://www.bookfinder.com/dir/e3cc/')
isbncomp('http://www.bookfinder.com/dir/e3cd/')
isbncomp('http://www.bookfinder.com/dir/e3ce/')
isbncomp('http://www.bookfinder.com/dir/e3cf/')
isbncomp('http://www.bookfinder.com/dir/e3d0/')
