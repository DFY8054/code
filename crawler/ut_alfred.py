# -*- coding:utf-8 -*-
import alfred
import urllib2
import re

theQuery = u'{query}'
result = ''
results = []

url = 'https://www.utrecsports.org/facilities/facility-schedules'
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
req = urllib2.Request(url, headers=hdr)
html = urllib2.urlopen(req).read()
html = re.sub('\s+', '', html)

regx = '<aname="\d{6}"></a>(.{1,30})</td>|<td>(.{0,20})</td><td>(.{5,15})</td><td>InformalBadminton'
p = re.compile(regx)
items = re.findall(p, html)

location_map = {'Room348':'BEL', 'Room2.200(ct.3)':'RSC'}

cnt = 1
for i in range(len(items)):
    if (items[i][0] != ''):
        current_day = items[i][0].split(',')
    else:
        content = ' ' + str(current_day[0]) + ' ' + str(current_day[1]) + ' ' + str(location_map[items[i][1]]) + ' ' + str(items[i][1])  + ' ' + str(items[i][2])
        item = alfred.Item({'uid': cnt, 'arg': theQuery}, content, '')
        cnt = cnt+1
        results.append(item)

xml = alfred.xml(results)
alfred.write(xml)
