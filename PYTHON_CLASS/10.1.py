fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

lst = list()
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)

lst = sorted(lst, reverse=True)
for val, key in lst[:10]:
    print(val, key)

x = ['f', 'd', 'c']

print(x.index('d'))
x.reverse()
print(x)

x = {'x': 1, 'y': 3}
print(x)



x = ('red', 'blue', 'green', '1', '2', '7')

"""
print(x)
print(x[2])
print(max(x))

for list in x:
    print(list)


#unline list, tuples can't be changed, they are immutable
#same as a string

#can't change a tuple at all

#try to use tuples if the variable is tempoery. less mem is used

(x, y) = (4, 'fred')
print(y)

#,items gives a list full of tuple

d = dict()

d['red'] = 2
d['blue'] = 3

for (k, v) in d.items():
    print(k, v)

tups = d.items()
print(tups)

x = (0, 1, 4) > (3, 4, 7)
print(x)

x = ('cake', 'rodger') > ('cool', 'blue')

# c = c, a in cake is not greater than o in cool so it's false
#never goes to the 2nd pair if the 1st pair is being worked on

print(x)

#have a dic, change into a tuple using .item, then sorted function to sort tuple

x = {'red': 1, 'blue': 7, 'reddy': 4}
x.items()
print(sorted(x))

#key ordered
for k, v in sorted(x.items()):
    print(k, v)


#value ordered
x = {'red': 1, 'blue': 7, 'reddy': 4}
tmp = list()
for k, v in x.items():
    tmp.append((v, k))
print(tmp)

tmp = sorted(tmp, reverse=True)
print(tmp)
"""

