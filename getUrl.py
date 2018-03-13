#!/usr/bin/env bash

import re, urllib, time

try:
    import urllib.request
except:
    pass

sites = 'google cnn msn yahoo'.split()

for s in sites:
    print('searching: ' + s)

    try:
        u = urllib.urlopen('http://' + s + '.com')
    except:
        u = urllib.request.urlopen('http://' + s + '.com')

    text = u.read()
    # title = re.findall(r'(<title>+.*</title>+)', str(text), re.I|re.M)
    # print(title[0])

    rand = str(time.time())
    rand = rand.split('.')

    try:
        file = open('logs/'+s+'_'+rand[1]+'.txt', 'w')
        file.write(str(text))
    except IOError:
        pass
