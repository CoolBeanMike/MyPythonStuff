numlist = list()

while True:
    inp = input('Input a number here: ')
    if inp == 'done':break
    value = float(inp)
    numlist.append(value)
print(numlist)

average = sum(numlist) / len(numlist)

print(average)


abc = 'cool one two dsa sad f erdf f sdf sdf sdf ds'
abc = abc.split()
print(abc)
print(abc[4])

for x in abc:
    print(x)
