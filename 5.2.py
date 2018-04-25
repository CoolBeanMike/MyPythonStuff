"""x = 0
while x < 5:
    print('cool')
    x = x + 1
    continue

for x in [10,9,8,7,6,5,4,3,2,1,0]:
    print(x)

print("blast off")


friends = ['sally', 'mike', 'tom']
dogs = ['cool', 'woo', 'low']
for friend in friends:
    print("happy new year: %s" % friend)
print('done')
"""


largest_so_far = -1
for the_num in [9, 41, 2828282, 12, 3, 74, 15, 10, 34, 765, 9797]:
    if the_num > largest_so_far:
        largest_so_far = the_num
        print("largest number so far is: ", largest_so_far)

print(largest_so_far)
