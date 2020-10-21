"""
Find_two_intergers_mult_to_20

1. ask yourself how will you find the answer on paper

2. so start like this

you have a 2 is there a 10
you have a 4, is there a 5
you have a 1 is there a 20
6 is no good, not divisible by 20
5 already found
40, is there a 0.5
-1 is there a -20

3. how about a list 100000 digets long?

4. what are multiples of 20

1 x 20
2 x 10
4 x 5

so is there a 1, 20, 2, 10, 4, 5



x = [2, 4, 1, 6, 10, 5, 40, -1, 20]

if (1 and 20) in x:
    print("we are good")
    print()
else:
    print("not found")

if (2 and 10) in x:
    print("we are good")
    print()
else:
    print("not found")

if (4 and 5) in x:
    print("we are good")
    print()
else:
    print("not found")

"""


x = list("2dfg5f3423sdwe")

print(x)

print(any(x))
print(bytearray(1))

def coolbean1(str):
    y = []
    for char in str:
        try:
            if char == "d":
                char1 = char.upper()
                y.append(char1)
            else:
                y.append(char)
        except Exception as e:
            print("Bad error" , e)

    print(' '.join(y))

coolbean1(x)
coolbean1("sdfg3456")


x = 8%3
x = 9/2
print(round(x,2))

#print(hex(x))

print(pow(3,3))

x = range(1,10)
for num in x:
    print(num)

x = [2,3,4,5]

print(tuple(x))

x = {'color':'blue', 'animal': 'dog'}
y = {'length':'inches', 'weight': 'pounds'}

print(tuple(x))

print(x.keys())
print(x.values())
print(x.items())

x.update(y)
print(x)

x = {'color': 'red'}
x['color'] = 'blue'
print(x)

x = [2,3,4,5,6]
y = ['q', 'w', 'e', 'r', 't', 't', 'q', 'q', 'q']
z = []

for char in y:
    x.append(char)

print(x)
x.remove('q')
print(x)

print(y.count('t'))
y.reverse()
print(y)
print(y)
print(y.index('q'))


s = "the cat is cool is great"
q = "eee fff hhh sss cc"
print(s.index('is'))

print(x.pop(3))

print(x[1:3])

print(s.capitalize())
print(s.upper())
print(s.lower())

h1 = ['q', 'w', 'e', 'r', 't', 't', 'q', 'q', 'q']
h2 = ''.join(h1)
h2 = 'BBB'.join(h1)
print(h2)

h3 = {'length':'inches', 'weight': 'pounds'}
s = ','
h4 = s.join((h3))
print(h4)

print("######################")
j = 'sss sss dfdd ggg s a s'
print(j.rstrip('ggg s s'))
print(j.lstrip('sss '))
print(j.strip(' sssdf'))
string = 'android is awesome'
print(string.strip('aw'))
print(string.strip('is'))
