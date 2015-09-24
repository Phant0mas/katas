#!/usr/bin/python3.4
# This file is published under the 3-clause BSD license
# Copyright 2015 Manolis Fragkiskos Ragkousis
# Check the license file.
import urllib.request

f = open('hosts.txt', 'r')
lines = [line.rstrip('\n') for line in f]

for i in range(len(lines)):
    data = lines[i].split(",")
    host=data[0]
    domain=data[1]
    password=data[2]
    
    url = 'https://dynamicdns.park-your-domain.com/update?host=' + host + \
          '&domain=' + domain + '&password=' + password + '&ip='
    print(url)

    response = urllib.request.urlopen(url)
    print(response.read().decode('utf-8'))
