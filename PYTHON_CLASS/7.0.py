"""
file_handle = open('windowsSESPARSEtest.py', 'r')
for stuff in file_handle:
    stuff = stuff.rstrip()
    if stuff.startswith('#'):
        print(stuff)
"""

try:
    file_name = input('Enter filename: ')
except Exception as wow:
    print('file can\'t be open', file_name, wow)
    quit()

new_file_handle = open(file_name, 'r')

count = 0

for line in new_file_handle:
    count = count + 1
    line = line.rstrip()
    if not line.startswith('if'):
        continue
    print(line)
print('The numbers of lines: ', count)
