"""When people send messages on their phones they sometimes modify word spelling by adding extra letters for emphasis. For example if you want to emphasize 'hello' you might write it 'hellloooooooo'. We’ll be calling the extra letters a 'word extension'.

Assumption: Regular text contains 2 or fewer of the same character in a row, while word extensions have 3 or more of the same character in a row.

Question: Given an input string representing one word, find the start and end indices of all extensions in the word. For example:
'heeeello' should return [1,4].

coooolbeanmikeee
[1,4, 13, 15]

"""

word = list('cdoooooolllg')

length = len(word) -1   # 5
len1 = int(0)
len2 = int(0)
count = int(0)

# index is between 0 and 4, but wil need to include 5 because end it chopped off

while count < length:
    if word[len1] == word[len2+1]:
        start_index = len1
        end_index = len2+1
        len2 += 1
        count += 1

    else:
        len1 += 1
        len2 += 1
        count += 1

print(start_index)
print(end_index)