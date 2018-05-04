"""
5.2 Write a program that repeatedly prompts a user for integer numbers
until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers.

If the user enters anything other than a valid
number catch it with a try/except and put out an appropriate message and ignore the number.

Enter 7, 2, bob, 10, and 4 and match the output below.
"""
import pdb


largest = None
smallest = None

while True:
    try:
        pdb.set_trace()
        number = int(input("Enter a number: "))
        if number == 'done':
            break

        if largest is None:
            largest = number

        elif number > largest:
            largest = number

        if smallest is None:
            smallest = number
        elif smallest < number:
            number = smallest


    except Exception as e:
        print("Enter a real number")
        continue

smallest = int(number)
largest = int(number)
