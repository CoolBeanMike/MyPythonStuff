"""
Find_two_intergers_mult_to_20

1. ask yourself how will you find the answer on paper

2. so start like this

you have a 2 is there a 10
you have a 4, is there a 5
you have a 1 is there a 20
6 is no good, not divisible by 20
5 already found
40, is there a 0.5
-1 is there a -20

3. how about a list 100000 digets long?

4. what are multiples of 20

1 x 20
2 x 10
4 x 5

so is there a 1, 20, 2, 10, 4, 5

"""

x = [2, 4, 1, 6, 10, 5, 40, -1, 20]

if (1 and 20) in x:
    print("we are good")
    print()
else:
    print("not found")

if (2 and 10) in x:
    print("we are good")
    print()
else:
    print("not found")

if (4 and 5) in x:
    print("we are good")
    print()
else:
    print("not found")

x = "2dfg5f3423sdwe"

print(list(x))