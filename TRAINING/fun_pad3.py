"""
Write a software test case for even numbers ??
-80 = even number
2 = even number
etc

"""

numbers = int(input("Enter a number: "))

for i in range(0, numbers):
    if (i%2) == 0:
        print(i)
        print(-i)


