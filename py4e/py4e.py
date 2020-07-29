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




# # the following is for twitter api and is ideally split between multiple files.
# # hidden.py # this file contains the oauth key
# def oauth():
#     return {"consumer_key": "something here",
#             "consumer_secret": "secret here",
#             "token_key": "key here",
#             "token_secret": "secret here"}

# # twtest.py
# import urllib.request, urllib.parse, urllib.error
# from twurl import augment
# import ssl

# print('* Calling Twitter...')
# url = augment('https://api.twitter.com/1.1/statuses/user_timeline.json', {'screen_name': 'drchuck', 'count': '2'}) # this is from twitter documentation to get user timeline info
# print(url)

# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# connection = urllib.request.urlopen(url, context=ctx)
# data = connection.read()
# print(data)

# # twitter1.py
# import urllib.request, urllib.parse, urllib.error
# import twurl
# import ssl

# TWITTER_URL = 'https://api.twitter.com/1.1/statuses/user_timeline.json'

# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# while True:
#     print('')
#     acct = input('Enter Twitter Account:')
#     if (len(acct) < 1): break
#     url = twurl.augment(TWITTER_URL, {'screen_name': acct, 'count': '2'})
#     print('Retrieving', url)
#     connection = urllib.request.urlopen(url, context=ctx)
#     data = connection.read().decode()
#     pritn(data[:250])
#     headers = dict(connection.getheaders())
#     pritn('Remaining', headers['x-rate-limit-remaining'])




# class PartyAnimal:
#     x=0

#     def __init__(self): # this is the constructor
#         print('I am constructed')

#     def party(self):
#         self.x += 1
#         print("So far", self.x)

#     def __del__(self): # destructor
#         print('I am destructed', self.x)
    
# an = PartyAnimal() # this is constructing the instance, and triggers the __init__ print
# an.party()
# an.party()
# an.party()
# an = 42 # overwriting an for now, which will trigger the __del__ print
# # print(type(an))
# # print(dir(an))



# class PartyAnimal:
#     x=0
#     name = ""

#     def __init__(self, z): # z is a parameter to pass in, in this case sally and jim
#         self.name = z
#         print(self.name, "constructed")

#     def party(self):
#         self.x += 1
#         print(self.name, "party count", self.x)

# s = PartyAnimal("Sally")
# s.party()
# j = PartyAnimal("Jim")
# j.party()
# s.party()


# class PartyAnimal:
#     x=0
#     name = ""
#     def __init__(self, nam):
#         self.name = nam
#         print(self.name, "constructed")

#     def party(self):
#         self.x += 1
#         print(self.name, "party count", self.x)
        
# class FootballFan(PartyAnimal): # this creates the child inheritance 
#     points = 0
#     def touchdown(self):
#         self.points += 7
#         self.party()
#         print(self.name, "points", self.points)

# s = PartyAnimal('Sally')
# s.party()
# j = FootballFan('Jim')
# j.party()
# j.touchdown()


# simple definitions:
# Class       -   a template
# Attribute   -   a variable within a class
# Method      -   a function within a class
# Object      -   a particular instance of a class
# Constructor -   code that runs when an object is created
# Inheritance -   the ability to extend a class to make a new class



# # emaildb.py
# import sqlite3

# conn = sqlite3.connect('emaildb.sqlite') # checks the connection to the file, since file doesn't exist, it will create this file when it runs
# cur = conn.cursor() # kinda like the handle...to read the file..SQL commands are sent through this cursor, and response is accepted through this cursor

# cur.execute('DROP TABLE IF EXISTS Counts') # drops emaildb table if exists, do nothing otherweise

# cur.execute('''
# CREATE TABLE Counts (email TEXT, count INTEGER)''')
# # goal below is to loop through a file like before, then for each email it finds, check if email exists, and update if it does
# fname = input('Enter file name: ')
# if (len(fname) < 1): fname = 'mbox-short.txt'
# fh = open(fname)
# for line in fh:
#     if not line.startswith('From: '): continue
#     pieces = line.split()
#     email = pieces[1]
#     cur.execute('SELECT count FROM Counts WHERE email = ?', (email,)) # email, so it is a tuple...weird python syntax thing. we want tuple here instead of just email. this line is not retrieving the data, but it is verifying table name, syntax is right, and is opening a record set.
#     row = cur.fetchone() # grab first one which matches above criteria of matching email, return it as row
#     if row is None: # if no records that meet this criteria
#         cur.execute('''INSERT INTO Counts (email, count)
#                 VALUES (?, 1)''', (email,)) # set count to 1 because None
#     else:
#         cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', (email,)) # updating instead of adding...just better for databases
#     conn.commit() # in this code it's committing every loop, but it can run every 10 loops or whatever

# # https://www.sqlite.org/lang_select.html
# sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10' # pulling data from db

# for row in cur.execute(sqlstr): # execute, pritn each row which is a tuple, which is why row[0] etc
#     print(str(row[0]), row[1])

# cur.close()



# # twspider.py
# from urllib.request import urlopen
# import urllib.error
# import twurl
# import json
# import sqlite3
# import ssl

# TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

# conn = sqlite3.connect('spider.sqlite')
# cur = conn.cursor()

# cur.execute('''
#             CREATE TABLE IF NOT EXISTS Twitter
#             (name TEXT, retrived INTEGER, friends INTEGER)''')

# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# while True:
#     acct = input('Enter a Twitter account, or quit: ')
#     if (acct == 'quit'): break
#     if (len(acct) < 1):
#         cur.execute('SELECT name FROM Twitter WHERE retrieved = 0 LIMIT 1')
#         try:
#             acct = cur.fetchone()[0]
#         except:
#             print('No unretrieved Twitter accounts found')
#             continue

#     url = twurl.augment(TWITTER_URL, {'screen_name': acct, 'count': '5'})
#     print('Retrieving', url)
#     connection = urlopen(url, context=ctx)
#     data = connection.read().decode()
#     headers = dict(connection.getheaders())

#     print('Remaining', headers['x-rate-limit-remaining'])
#     js = json.loads(data)

#     cur.execute('UPDATE Twitter SET retrieved=1 WHERE name = ?', (acct, ))

#     countnew = 0
#     countold = 0
#     for u in js['users']:
#         friend = u['screen_name']
#         print(friend)
#         cur.execute('SELECT friends FROM Twitter WHERE name = ? LIMIT 1', (friend, ))
#         try:
#             count = cur.fetchone()[0]
#             cur.execute('UPDATE Twitter SET friends = ? WHERE name = ?', (count+1, friend))
#             countold += 1
#         except:
#             cur.execute('''INSERT INTO Twitter (name, retrieved, friends)
#                             VALUES (?, 0, 1)''', (friend, ))
#             countnew += 1
#     print('New accounts=', countnew, ' revisted=', countold)
#     conn.commit()
# cur.close()




# # tracks.py
# import xml.etree.ElementTree as ET # reads xml
# import sqlite3 # reads sqlite db

# conn = sqlite3.connect('trackdb.sqlite') # creates db if doesn't already exist
# cur = conn.cursor()

# # Make some fresh tables using executescript()
# cur.executescript('''
# DROP TABLE IF EXISTS Artist;
# DROP TABLE IF EXISTS Album;
# DROP TABLE IF EXISTS Track;

# CREATE TABLE Artist (
#     id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#     name    TEXT UNIQUE
# );

# CREATE TABLE Album (
#     id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#     artist_id  INTEGER,
#     title   TEXT UNIQUE
# );

# CREATE TABLE Track (
#     id  INTEGER NOT NULL PRIMARY KEY 
#         AUTOINCREMENT UNIQUE,
#     title TEXT  UNIQUE,
#     album_id  INTEGER,
#     len INTEGER, rating INTEGER, count INTEGER
# );
# ''') # create these tables fresh if they dne


# fname = input('Enter file name: ')
# if ( len(fname) < 1 ) : fname = 'Library.xml' # apples xml...as mentioned would be a lot better in json

# # <key>Track ID</key><integer>369</integer>
# # <key>Name</key><string>Another One Bites The Dust</string>
# # <key>Artist</key><string>Queen</string>
# def lookup(d, key): # key is second due to how this xml was designed
#     found = False
#     for child in d:
#         if found : return child.text
#         if child.tag == 'key' and child.text == key :
#             found = True
#     return None

# stuff = ET.parse(fname)
# all = stuff.findall('dict/dict/dict') # goes down to 3rd level of dict which contains track info
# print('Dict count:', len(all))
# for entry in all:
#     if ( lookup(entry, 'Track ID') is None ) : continue

#     name = lookup(entry, 'Name')
#     artist = lookup(entry, 'Artist')
#     album = lookup(entry, 'Album')
#     count = lookup(entry, 'Play Count')
#     rating = lookup(entry, 'Rating')
#     length = lookup(entry, 'Total Time')

#     if name is None or artist is None or album is None : 
#         continue

#     print(name, artist, album, count, rating, length)

#     cur.execute('''INSERT OR IGNORE INTO Artist (name) 
#         VALUES ( ? )''', ( artist, ) ) # because artist name is unique, it will blow up if inserting duplicate artist name, therefore insert or ignore
#     cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, )) # select above artist id
#     artist_id = cur.fetchone()[0]

#     cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
#         VALUES ( ?, ? )''', ( album, artist_id ) )
#     cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
#     album_id = cur.fetchone()[0]

#     cur.execute('''INSERT OR REPLACE INTO Track
#         (title, album_id, len, rating, count) 
#         VALUES ( ?, ?, ?, ?, ? )''', # similar to above, except this replaces instead of ignores
#         ( name, album_id, length, rating, count ) )

#     conn.commit()






