"""
8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the
split() method. The program should build a list of words. For each word on each line check to see if the word is
already in the list and if not append it to the list. When the program completes, sort and print the resulting words
in alphabetical order. You can download the sample data at http://www.py4e.com/code3/romeo.txt
"""

#fname = input('Enter file name: ')
#fh = open(fname)

fh = open('romeo.txt')
lst = list()
tnd = list()
for line in fh:
    words = line.split()
    for word in words:
        lst.append(word)
print(lst)

start = 0
inc = 0
print(len(lst))

while start < len(lst):
    if lst[start] != lst[inc+1]:
        tnd.append(lst[inc+1])
        inc = inc + 1
        if inc == len(lst):
            start = start + 1

print(tnd)

#inc = inc + 1
#print(start)


#for line in words:
#    lst.append(words)

#print(lst)

    #for word in words:
    #    lst.append(word)
    #print(lst)



#y = len(lst)
#for x in range(0, y):
#    print(lst[x])
