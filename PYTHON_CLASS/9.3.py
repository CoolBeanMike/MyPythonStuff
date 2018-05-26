"""
counts2 = dict()
line = input("please enter text here:")
words = line.split()
print('words', words)
for word in words:
    counts2[word] = counts2.get(word, 0) + 1

print('Counts:', counts2)

for key in counts2:
    print(key, counts2[key])
    print(counts2.keys())
    print(counts2.values())
    print(counts2.items())

counts2 = {'sasa': 1, 'red': 3, 'gggg': 67}
for key, value in counts2.items():
    print(key, value)


counts2 = dict()
line = open('mbox-short.txt')
for x in line:
    words = x.split()
    print('words', words)

"""
name = input('enter a file: ')
handle = open(name)
counts = dict()

for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)
"""
maxcount = None
maxname = None

for word, counts in counts.items():
    if maxcount is None or counts > maxcount:
        maxcount = counts
        maxname = name
print(maxname, maxcount)

"""
