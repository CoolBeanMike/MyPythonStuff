"""
Given an array say [0,1,2,3,5,6,7,11,12,14,20]
given a number say 5.
Now find the sum of elements which sum to 5
eg:2+3=5, 0+5=5 etc.
I guess the interviewer wanted all possible combinations eg 0+2+3=5, etc

so %

5+0, 0+1+4, 0+2+3
"""

zero = 0
one = 1
two = 2
three = 3
four = 4
five = 5

sum_of_numbers = []

numbers = [0,1,2,3,5,6,7,11,12,14,20]
for x in numbers:
    if x == zero or x == three or x == two:
        sum_of_numbers.append(x)
print(sum_of_numbers)
print(sum(sum_of_numbers))

sum_of_numbers = []

for x in numbers:
    if x == zero or x ==5:
        sum_of_numbers.append(x)
print(sum(sum_of_numbers))