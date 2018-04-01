###
#print(ord('H'))

#4 bytes per character
#utf-8 is the best, recomended, best to move data between systems japan to USA
#utf32 = fix 4 bytes
#utf16 = fixed 2 bytes

#python2 byte string and reg string are the same, unicode and reg string are diff
#python3, everyhting is unicode, reg string and byte string are diff, unicode and reg string are same
# 11:20 - 12:36
# decode stuff being pulled in

#When we read data from an external source we must decode it and make it a string

#import socket
#mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#mysock.connect(('data.pr4e.org', 80))
#cmd = 'GET http://data.pr4e.org/romio.txt HTTP/1.0\n\n'.encode()
#mysock.send(cmd)

#while True:
#    #bytes
#    data = mysock.recv(512)
#    if (len(data) < 1):
#        break
#    #unicode
#    mystring = data.decode()
#    print(mystring)

#before we send and receive we must encode/decode this stuff

# decode is a method in the bytes class
# encode is in the srings class
# 16:10

###
#urllib.

import urllib.request , urllib.parse, urllib.error
#opena file handle
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt ')
for line in fhand:
    #line is a byte array
    print(line.decode().strip())

#12.4 --> grab links in a web page 5:27


