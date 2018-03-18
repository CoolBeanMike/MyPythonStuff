
import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:', line):
        print(line)


hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    # ^ means 'F' is the first character in the line
    if re.search('^From:', line):
        print(line)

"""
# ^X.*: ---> X in the beginning, followed by any number of characters followed by a :
# ^F.+:  ---> First character in the match is F, . = any character, + means one or more characters , : means last character to match

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    # ^ means 'F' is the first character in the line
    if re.search('^X.*:', line):
        print(line)

import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    # ^ means 'F' is the first character in the line
    if re.search('^X-\S+:', line):
        print(line)


x = 'In\'m cOol 234 to thE 56 hilt'
#get a list of matches and returns a string (one or more didgets
y = re.findall('[0-9]+', x)
print(y)


y = re.findall('[AEIOU]+', x) # look for AEIOU, + means greater than equal or equal to 1
print(y)


x = 'From ssasaasdasd.dsadsdasdsa@coolbean.com  dsadsad  dsadsa  dsadsd'
# At least one non-whitespace character
print(re.findall('\S+@\S+', x))

#Look for From but the exclosing () say I want everyhting after the "From "
# Extract (From )
y = re.findall('^From (\S+@\S+)', x)
print(y)

#extract everying after the @ sign that is non blank characters in an email address so --> ibm.com
# '@([^ }*)'  []= Match non-blank characters, * = Match many of them
# everything but a space
y = re.findall('@([^ ]*)', x)
print(y)

"""