try:
    hrs = float(input("Enter Hours Worked: "))
except:
    print('bad time')
    hrs = float(input("Enter Hours Worked: "))

try:
    payRate = float(input("Enter Pay Rate per hour: "))
except:
    print('bad pay rate')
    payRate = float(input("Enter Pay Rate per hour: "))

if hrs > 40:
    addHr = hrs - 40
    print(40 * payRate + payRate*1.5 * addHr)
else:
    print(payRate * hrs)
