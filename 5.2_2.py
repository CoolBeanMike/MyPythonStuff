largest = None
smallest = None
total = 0
count = 0

while True:
    try:
        num = input('Enter a number: ')
        if num == 'done':
            break

        num = int(num)

        if largest is None:
            largest = num
        elif num > largest:
            largest = num

        if smallest is None:
            smallest = num
        elif num < smallest:
            smallest = num

        total = num + total
        count = 1 + count
        Ave = float(total/count)

    except Exception as e:
        print('Invalid input')
        continue

print('Maximum is', largest)
print('Minimum is', smallest)
print('total', total)
print('count', count)
print('Ave', Ave)
