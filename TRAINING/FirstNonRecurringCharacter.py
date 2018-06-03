"""
# First Non Recurring Character

# DABBFA --> F

"""

import collections

def firstUnique(text):
    counts = collections.defaultdict(int)
    for letter in text:
        counts[letter] += 1
    for letter in text:
        if counts[letter] == 1:
            return letter


print(firstUnique("AABBCCCCEXEE"))
