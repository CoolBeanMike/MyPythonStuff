"""
have a string and you reverse it

x = "abcdefg"

"""
x = "abcdefg"
y = []

length = len(x)
print(length)
print(list(x))
len1 = length

while len1 > 0:
    y.append(x[len1-1])
    len1 -= 1

print(' '.join(y))


s = '1235'

print(list(s))

z = list(s)

x = ' '.join(z)
print(x)

print(set(s))

print((tuple(s)))

dic_1 = {'color': 'red', 'animal':'dog'}

element = dic_1.pop('animal')

print(element)

x = "the cat is a good cat"

print(type(x))
print(x.find('is'))

cool = ['s', 'a']

print(sorted(cool))