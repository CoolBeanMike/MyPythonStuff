"""
have a string, find the index of the first letter in the word of choice

x = ("does the cat like to eat grass", "cat")

answer:
WORD = cat
index is 7 --> where c is
if word is not found return -1

"""

#x = "does the cat like to eat grass, cat"

"""

###### Take a string and return the fist recurring character in it
# return B
y = "BCABCCBBBA"
#store in a hash table AKA dictionary
counts = {}
number = int(1)
for char in y:
    if char in counts:
        number += 1
        #print(char, number)
        break
    count[char] = 1

"""
###### Take a string and return the fist non recurring character in it
# return B
y = "SSXSCCBBCAXBCCBBBA"
#store in a hash table AKA dictionary
counts = {}
for char in y:
    if char in counts:
        #print(char)
        continue
    counts[char] = 1
    print(counts)
    break

"""
#type in words and find repeat ones and count number of words
counts2 = {}
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


"""
"""
counts2 = dict()
line = open('mbox-short.txt')
for x in line:
    words = x.split()
    print('words', words)
"""