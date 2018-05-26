"""
3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error.
If the score is between 0.0 and 1.0, print a grade using the following table:
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.
"""

score = float(input('Input Grade here: '))

if score > 1:
    print("out of range")
    exit(-1)
if score < 0:
    print('out of range')
    exit(-1)
elif score >= 0.9:
    print('you got an A')
elif score >= 0.8:
    print('you got a B')
elif score >= 0.7:
    print('you got an C')
elif score >= 0.6:
    print('you got a D')
elif score < 0.6:
    print('you got an F')
