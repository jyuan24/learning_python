# Python for Everybody - Full Course with Dr. Chuck
# https://www.youtube.com/watch?v=8DvywoWv6fI

# inp = input('Europe floor? ')
# usf = int(inp) + 1
# print('US floor', usf)


# fhand = open('open_test.txt')
# inp = fhand.read()
# print(len(inp))
# print(inp[:20])
# count = 0
# for line in fhand:
#     count += 1
# print('Line Count', count)



# # name = input('Enter file: ')
# handle = open('mbox-short.txt')
#
# for line in handle:
#     line = line.rstrip()
#     words = line.split()
#     # guardian
#     if len(words) < 3 or words[0] != 'From' :
#         continue
#     print(words[2])


# counts = dict()
# names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
# for name in names:
#     # do the below instead of if name exists, counts[name] = counts[name] + 1
#     counts[name] = counts.get(name, 0) + 1
# print(counts)


# handle = open('mbox-short.txt')
# counts = dict()
# for line in handle:
#     words = line.rsplit()
#     for word in words:
#         counts[word] = counts.get(word, 0) + 1
# for key, value in counts.items():
#     print(key, value)
# bigcount = None
# bigword = None
# for word, count in counts.items():
#     if bigcount is None or count > bigcount:
#         bigword = word
#         bigcount = count
# print(bigword, bigcount)




# c = {'a':10, 'b':1, 'c':22}
# tmp = list()
# print(tmp)
# for k,v in c.items():
#     tmp.append( (v,k) )
# print(tmp)
# tmp = sorted(tmp, reverse=True)
# print (tmp)


# fhand = open('romeo.txt')
# counts = dict()
# for line in fhand:
#     words = line.rsplit()
#     for word in words:
#         counts[word] = counts.get(word, 0) + 1
# print (counts)
# # below can also be done with:
# # print( sorted( [ (v,k) for k,v in counts.items() ], reverse=True ) )
# lst = list()
# for k,v in counts.items():
#     lst.append((v,k))
# lst = sorted(lst, reverse=True)
# for v,k in lst[:10]:
#     print (v,k)



# fname = input('Enter File: ')
# if len(fname) < 1: fname = 'clown.txt'
# hand = open(fname)
#
# di = dict()
# for lin in hand:
#     lin = lin.rstrip()
#     wds = lin.split()
#     for w in wds:
#         di[w] = di.get(w,0) + 1
# print(di)
#
# x = di.items()
# print(x)
#
# x = sorted(di.items())
# print(x[:5])
#
# tmp = list()
# for k,v in di.items():
#     newt = (v,k)
#     tmp.append(newt)
#     print (k,v)
# print(tmp)
#
# tmp = sorted(tmp, reverse=True)
# print (tmp[:10])
# for v,k in tmp[:5]:
#     print (k,v)



# import re
# # x = 'My 2 favorite numbers are 19 and 42'
# # y = re.findall('[0-9]+', x)
# # print(y)
# # y = re.findall('[AEIOU]+', x)
# # print(y)
#
# hand = open('mbox-short.txt')
# numlist = list()
# for line in hand:
#     line = line.rstrip()
#     stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
#     if len(stuff) != 1: continue
#     num = float(stuff[0])
#     numlist.append(num)
# print('Maximum:', max(numlist))



# import socket
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect( ('data.pr4e.org', 80) )



# # writing a web browser
# import socket
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80)) # begin connect to http port 80
# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode() # gets data, with 2 blank lines after as required. .encode converts unicode to utf8
# mysock.send(cmd)
#
# while True:
#     data = mysock.recv(512) # return 512 characters at a time, until no more characters
#     if (len(data) < 1):
#         break
#     print(data.decode()) # decoding utf8 to unicode
# mysock.close() # close the socket
# unicode is characters we understand, but take sup 4 bytes / character, whereas utf8 only takes 1-4 bytes/character. utf8 is recommended practice for encoding data to be exchanged between systems
# in python, all strings are unicode
# when scraping web, data we get back will be some sort of bytes, would have to figure out if it is string, unicode or what. most of the time it should be utf8 which would include ascii which would be ideal



# import urllib.request, urllib.parse, urllib.error
# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt') # this line with urlopen encodes automatically, and returns an object that looks like an object handle
# for line in fhand:
#     print(line.decode().strip()) # file still comes back as bytes, so decode still necessary
# # notice headers are not shown, but it is still involved in urlopen, just need to specify to show headers
#
# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# counts = dict()
# for line in fhand:
#     words = line.decode().split()
#     for word in words:
#         counts[word] = counts.get(word, 0) + 1
# print(counts)


# # reading web pages html instead of txt
# import urllib.request, urllib.parse, urllib.error
# fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
# for line in fhand:
#     print(line.decode().strip())
# # info comes back as html with tags
# # guessing python was used for google to scrape web info?
# # now how to handle the tags?



# import urllib.request, urllib.parse, urllib.error
# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# counts = dict()
# for line in fhand:
#     print(line.decode().strip())
#     words = line.decode().split()
#     for w in words:
#         counts[w] = counts.get(w, 0) + 1
# print(counts)


# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup





# # http://www.py4e.com/code3/bs4.zip
# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup
# import ssl # required for websites w/ ssl (HTTPS as opposed to HTTP)
#
# # ignore ssl certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
#
# url = input('Enter - ') # ask user for url
# html = urllib.request.urlopen(url, context=ctx).read() # same as before, but now read would return entire doc as a single big string. doesn't matter if it's utf8 or unicode
# soup = BeautifulSoup(html, 'html.parser') # beautifulsoup can deal with those formats and deal with all the tags
#
# # retrieve all of the anchor tags
# tags = soup('a') # gets all a tags from doc
# for tag in tags:
#     print(tag.get('href', None)) # returns list of hrefs in document




# using xml...similar to json...to send info across the net..below is json example
# {
#     "name": "Chuck"
#     "phone": "303-4456"
# }
# xml - extensible markup language
# xml uses tags to indicate beginning and end of element, attributes which are key/value pairs, serialize/deserialize to convert into common format between programming languages
# basic xml below
# <person> # start tag
#     <name>Chuck</name>
#     <phone type="intl"> # attribute type
#         #1 734 303 4456
#     </phone>
#     <email hide="yes"/>
# </person> # end tag
# similar to html, but see it as a tree to show all parent/child relations. above name, phone are embedded in person


# import xml.etree.ElementTree as ET
# data = '''
# <person>
#     <name>Chuck</name>
#     <phone type = "intl">
#         +1 734 303 4456
#     </phone>
#     <email hide="yes"/>
# </person>'''
#
# tree = ET.fromstring(data)
# print('Name:', tree.find('name').text) # to get text
# print('Attr:', tree.find('email').get('hide')) # to get attribute

# import xml.etree.ElementTree as ET
# input = '''
# <stuff>
#     <users>
#         <user x="2">
#             <id>001</id>
#             <name>Chuck</name>
#         </user>
#         <user x="7">
#             <id>007</id>
#             <name>Brent</name>
#         </user>
#     </users>
# </stuff>'''
# stuff = ET.fromstring(input)
# lst = stuff.findall('users/user')
# print('User count:', len(lst))
# for item in lst:
#     print('Name', item.find('name').text)
#     print('Id', item.find('id').text)
#     print('Attribute', item.get("x"))


# import xml.etree.ElementTree as ET
# data = '''
# <person>
#     <name>Chuck</name>
#     <phone type='intl'>
#         +1 734 303 4456
#     </phone>
#     <email hide='yes'/>
# </person>'''
# tree = ET.fromstring(data)
# print('Name:', tree.find('name').text)
# print('Attr:', tree.find('email').get('hide'))



# # similar json representation of the above
# import json
# data = '''
# {
#     "name" : "Chuck",
#     "phone" : {
#         "type" : "intl",
#         "number" : "+1 734 303 4456"
#     },
#     "email" : {
#         "hide" : "yes"
#     }
# }'''
# info = json.loads(data)
# print('Name:', info["name"])
# print('Hide:', info["email"]["hide"])


# # if json data was a list instead of a dictionary
# import json
# input = '''
# [
#     {
#         "id" : "001",
#         "x" : "2",
#         "name" : "Chuck"
#     },
#     {
#         "id" : "009",
#         "x" : "7",
#         "name" : "Chuck"
#     }
# ]'''
# info = json.loads(input)
# print('User count:', len(info))
# for item in info:
#     print('Name', item['name'])
#     print('Id', item['id'])
#     print('Attribute', item['x'])




# # https://api.github.com/users/jyuan24
# import urllib.request, urllib.parse, urllib.error
# import json
# # serviceurl = 'https://api.github.com/users/'
# serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
# while True:
#     username = input('Enter location: ')
#     if len(address) < 1: break
#     url = serviceurl + urllib.parse.urlencode({'address': address}) # this will result in a 'username=jyuan24' in address...not ideal...
#     print('Retrieving', url)
#     uh = urllib.request.urlopen(url)
#     data = uh.read().decode()
#     print('Retrieved', len(data), 'characters')
# try:
#     js = json.loads(data)
# except:
#     js = None
# if not js or 'status' not in js or js['status'] != 'OK':
#     print('==== Failure To Retrieve ====')
#     print(data)
#     continue
# print(json.dumps(js, indent=4)) # prints so json comes back with indents in console
# lat = js['results'][0]['geometry']['location']['lat']
# lng = js['results'][0]['geometry']['location']['lng']
# print('lat', lat, 'lng', lng)
# location = js['results'][0]['formatted_address']
# print(location)




# the following is for twitter api and is ideally split between multiple files.
# hidden.py # this file contains the oauth key
def oauth():
    return {"consumer_key": "something here",
            "consumer_secret": "secret here",
            "token_key": "key here",
            "token_secret": "secret here"}

# twtest.py
import urllib.request, urllib.parse, urllib.error
from twurl import augment
import ssl

print('* Calling Twitter...')
url = augment('https://api.twitter.com/1.1/statuses/user_timeline.json', {'screen_name': 'drchuck', 'count': '2'}) # this is from twitter documentation to get user timeline info
print(url)

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

connection = urllib.request.urlopen(url, context=ctx)
data = connection.read()
print(data)

# twitter1.py
import urllib.request, urllib.parse, urllib.error
import twurl
import ssl

TWITTER_URL = 'https://api.twitter.com/1.1/statuses/user_timeline.json'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    print('')
    acct = input('Enter Twitter Account:')
    if (len(acct) < 1): break
    url = twurl.augment(TWITTER_URL, {'screen_name': acct, 'count': '2'})
    print('Retrieving', url)
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()
    pritn(data[:250])
    headers = dict(connection.getheaders())
    pritn('Remaining', headers['x-rate-limit-remaining'])