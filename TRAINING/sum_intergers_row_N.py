"""
1
2  3
4  5  6
7  8  9  10
11 12 13 14 15

Row 1 = index 0:0
Row 2 = index 1:2
Row 3 = index 3:5
Row 4 = index 6:9
Row 5 = index 10:14
"""

print(1)
print(2+3)
print(4+5+6)
print(7+8+9+10)
print(11+12+13+14+15)

numbers = []
Row = 5
count = 0
total = 0

while count <= Row:
    row = Row - count
    count += 1
    total = row + total

for num in range(1, total + 1):
    numbers.append(num)

print("Whole List:", numbers)

index_row = 4
start = 0
x = 0

while start <= index_row:
    x = x + start
    start += 1
    print("index start:", x, "row:", start, "Row Sum:", sum(numbers[x:x+start]))








