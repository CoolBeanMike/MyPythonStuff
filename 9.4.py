#7:02
#8:40

"""
counts = dict()
names = ['red', 'blue', 'green', 'red', 'blue']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)

#below is the same

counts = dict()
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)
"""

"""
Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail 
messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they 
appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to 
find the most prolific committer.
"""


filename = input('Enter File Name: ')
fileopen = open(filename)

namesdic = dict()
nameslst = list()

maxcount = None
maxname = None

for line in fileopen:
    if 'From ' in line:
        x = line.split()
        nameslst.append(x[1])

for names in nameslst:
    namesdic[names] = namesdic.get(names, 0) + 1

for key, value in namesdic.items():
    if maxcount is None or value > maxcount:
        maxcount = value
        maxname = key
print(maxname, maxcount)


