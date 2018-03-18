import re

# variable and new list initialization
newlist = []
newsum = int(0)
count = int(0)

# opening file to be read
file = open("regex_sum_62808.txt")

# going through each line and plucking out numbers only
for line in file:
    line = line.rstrip()
    stuff = re.findall('[0-9]+', line)
    newlist.append(stuff)

# creating a list of only present strings
q = (sum(newlist, []))

# calculating the length of the list
z = len(sum(newlist, []))

# adding each of the values of the index to get a total
while count < z + 1:
    try:
        newsum = newsum + int(q[count])
        count = count + 1
    except:
        break

# printing the total of newsum
print(newsum)
