x = input("Please input a bunch of word: ")
y = []
length = len(x)
print(length)
print(list(x))
len1 = length

while len1 > 0:
    y.append(x[len1-1])
    len1 -= 1

print(' '.join(y))

"""
s = (1,2 ,3 ,5 )

print(set(s))
print(list(s))

print((tuple(s)))

"""