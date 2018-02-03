file_asked_for = input('Please enter a file name: ')
opened_file = open(file_asked_for, 'r')
for x in opened_file:
    x = x.rstrip().upper()
    print(x.rstrip().upper())
