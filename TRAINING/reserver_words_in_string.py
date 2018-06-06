z = []
x = input("Please input a bunch of word: ")

y = x.split()
print(y)

length = (len(y))
x = length
while x > 0:
    z.append(y[x-1])
    x -= 1

print(' '.join(z))


s = (1,2 ,3 ,5 )

print(set(s))
print(list(s))

print((tuple(s)))