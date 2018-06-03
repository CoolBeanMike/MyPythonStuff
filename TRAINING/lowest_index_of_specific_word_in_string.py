"""
have a string, find the index of the first letter in the word of choice

x = ("does the cat like to eat grass", "cat")

answer:
WORD = cat
index is 7 --> where c is
if word is not found return -1

"""

x = "does the cat like to eat grass"
print(x.find("cat"))

try:
    if x.find("cat") >= 0:
        print(x.find("cat"))

except Exception as e:
    print(-1)
