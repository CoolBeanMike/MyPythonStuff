"""
 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for
 each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting
 the string a second time using a colon.

 From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

 Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
"""

file = open('mbox-short.txt')

date = list()
counts = dict()

for line in file:
    if 'From ' in line:
        chop_up_from_line = line.split(' ')
        y = chop_up_from_line[6]
        time_split = (y.split(':'))
        hour = time_split[0]
        date.append(hour)

for word in date:
    counts[word] = counts.get(word, 0) + 1

for key, val in sorted(counts.items()):
    print(key, val)

