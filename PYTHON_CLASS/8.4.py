fname = input('Enter file name: ')
fh = open(fname)

lst = list()
tnd = list()
for line in fh:
    words = line.split()
    for word in words:
        lst.append(word)
for x in range(0, len(lst)):
    if lst[x] not in lst[x+1:]:
        tnd.append(lst[x])

tnd.sort()
print(tnd)
