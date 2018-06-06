"""
A = "ffgggtvshjsdhjfffffffhvjbjcharu"
Find the max consecutive repitative chracter
Output : f -> 7
"""
A = "ffgggtvshjsdhjfffffffhvjbjcharu"
thechar = None
first_char = A[0]
sum = 0
max_sum = 0

for x in A[1:]:
    if x == first_char:
        sum += 1
        char = x
        if sum > max_sum:
            max_sum = sum
            thechar = char
    else:
        first_char = x
        sum = 0

print("Sum:", max_sum, "The Character :", thechar)



