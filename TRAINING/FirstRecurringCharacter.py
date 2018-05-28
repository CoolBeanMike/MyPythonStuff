"""
# First Recurring Character

# D B C A B A --> B

# If I start With D, go down list, no matches
# Then I I go to B , go down list, matches B and we exit out

# Big-O conplexity is ----> Time Complexity or run time is ---> O(n^2)

#lets do better, use a hash tabe AKA dict
# go from left to right

# Big-O complexity is ----> Time Complexity or run time is ---> O(n), n is the number of characters in the string


Character     Count
D               1
B               2
C               1
A               1
"""


def first_recuring_string(str):
    table = {}
    for char in str:
        if char in table:
            return char
        else:
            table[char] = 1


print(first_recuring_string("ascccddeee"))
