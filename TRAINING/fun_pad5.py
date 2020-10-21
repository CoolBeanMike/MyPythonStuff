characters = "ABAACDDDBBA"
letter = {}
count = int(1)
maxcount = int(0)

print(characters)

for x in sorted(characters):
    if x in letter:
        count += 1
        letter[x] = count
        #if count > maxcount:
        #    maxcount = count
        #    count = 0
        #    continue
    else:
        count = 1
        letter[x] = count


print(letter)