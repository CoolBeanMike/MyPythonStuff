"""
A = "ffgggtvshjsdhjfffffffhvjbjcharu"
Find the max consecutive repitative chracter
Output : f -> 7
"""

A = "ffggggtv"

chardic= {}
num = int(1)
maxcharnum = None
charnum = 0


for char in A:
    if char in chardic:
        num = num + 1
        chardic[char] = num
        if num > maxcharnum:
            maxcharnum = num
        num

    chardic[char] = 1
    num = 1

print(chardic)