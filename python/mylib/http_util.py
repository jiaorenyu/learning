#!/usr/bin/python

import urllib2,urlparse

#default x-www-form-urlencoded
def httppost(host, action, data):
    url = urlparse.urljoin(host, action)
    print(url)
    return urllib2.urlopen(url, data).read()

def httppost_(host, action, data):
    opener = urllib2.build_opener()
    request = urllib2.Request(host+action, data, headers={"Content-Type": "text/plain"})
    return opener.open(request).read()

def httpget(host, action):
    url = urlparse.urljoin(host, action)
    return urllib2.urlopen(url).read()

if __name__ == "__main__":
    print "hello"
