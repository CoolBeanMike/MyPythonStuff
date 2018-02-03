fname = input('Please enter a file name: ')

fh = open(fname, 'r')

count = 0
total = 0
for line in fh:
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    count = count + 1
    total = total + float(line[len('X-DSPAM-Confidence:'):].strip())

total = total/count
print('Average spam confidence: ' + str(total))
