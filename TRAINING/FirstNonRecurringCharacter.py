"""
# First Non Recurring Character

# DABBFA --> F

"""


def first_non_recuring_string(str):
    table = {}
    first = None
    for char in str:
        if char in table:
            second = char
            if second == first:
                continue
            print("The first non occurring char: ", first)
        table[char] = 1
        first = char




print(first_non_recuring_string("aabbfa"))
