# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
#    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
#    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

'''
list1 = ["w", 1, "t"]
list2 = ["w", 1, "t"]

combined = list1 + list2

print (combined)

list1.extend(list2)

print (list1)

first_value = input("What is your first value: ")
second_value = 10
print ("Total: ", int(first_value) + second_value)


print("I have information for the following planets:\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")

weight = 185
planet = 3

# Write an if statement below:

planet = input("What world are you on:")

d = {'Venus': 0.91, 'Mars': 0.38, 'Jupiter': 2.34}

gravity = d[planet]

print (gravity)

print ("My weight on planet", planet, "is", weight*gravity)

###############################

user_name = "Dave"
match user_name:
    case "Dave":
        print("Get off my computer Dave!")
    case "angela_catlady_87":
        print("I know it is you, Dave! Go away!")
    case "Codecademy":
        print("Access Granted.")
    case default:
        print("Username not recognized.")


x = 0

if x == 0:3
  print("x is equal to zero")
elif x >= 0:
  print("x is greater than zero")
else:
  print("x is less than zero")


import random
question = input("What is your question today: ")

fortunes = ["Yes - definitely", "It is decidedly so", "Without a doubt", "Reply hazy, try again", "Ask again later", "Better not tell you now", "My sources say no", "Outlook not so good", "Very doubtful"]

random_number = random.randint(0, 8)

print ("Magic 8-Ball's answer:", fortunes[random_number])



weight = round(float(input("What is the weight of your package: ")),2)

if weight <= 2:
    ground_shipping = round(float(weight * 1.50 + 20), 2)
    drone_shipping = round(float(weight * 4.50), 2)
    premium_shipping = round(float(125), 2)
    print (ground_shipping, "a", drone_shipping, "a", premium_shipping)
    if ground_shipping < drone_shipping < premium_shipping:
        print("Ground shipping is the cheapest at a cost of:", ground_shipping)
    elif drone_shipping < premium_shipping:
        print ("Drone shipping is the cheapest at a cost of:", drone_shipping)
    else:
        print ("Premium shipping is the cheapest at a cost of:", premium_shipping)

if weight > 2 and weight <= 6:
    ground_shipping = round(float(weight * 3.00 + 20), 2)
    drone_shipping = round(float(weight * 9.00), 2)
    premium_shipping = round(float(125), 2)
    print (ground_shipping, "b", drone_shipping, "b", premium_shipping)
    if ground_shipping < drone_shipping < premium_shipping:
        print("Ground shipping is the cheapest at a cost of:", ground_shipping)
    elif drone_shipping < premium_shipping:
        print ("Drone shipping is the cheapest at a cost of:", drone_shipping)
    else:
        print ("Premium shipping is the cheapest at a cost of:", premium_shipping)

if weight > 6 and weight <=10:
    ground_shipping = round(float(weight * 4.00 + 20), 2)
    drone_shipping = round(float(weight * 12.00), 2)
    premium_shipping = round(float(125), 2)
    print (ground_shipping, "c", drone_shipping, "c", premium_shipping)
    if ground_shipping < drone_shipping < premium_shipping:
        print("Ground shipping is the cheapest at a cost of:", ground_shipping)
    elif drone_shipping < premium_shipping:
        print ("Drone shipping is the cheapest at a cost of:", drone_shipping)
    else:
        print ("Premium shipping is the cheapest at a cost of:", premium_shipping)

if weight > 10:
    ground_shipping = round(float(weight * 4.75 + 20), 2)
    drone_shipping = round(float(weight * 14.25), 2)
    premium_shipping = round(float(125), 2)
    print (ground_shipping, "d", drone_shipping, "d", premium_shipping)
    if ground_shipping < drone_shipping < premium_shipping:
        print("Ground shipping is the cheapest at a cost of:", ground_shipping)
    elif drone_shipping < premium_shipping:
        print ("Drone shipping is the cheapest at a cost of:", drone_shipping)
    else:
        print ("Premium shipping is the cheapest at a cost of:", premium_shipping)

x = 0
while x <= 2:
    print("red1", x)
    x += 1
else:
    print ("we are done")



customer_data = [["Ainsley", "Small", True], ["Ben", "Large", False], ["Chani", "Medium", True], ["Depak", "Medium", False]]

print (customer_data)

customer_data[2][2] = False

print (customer_data)

customer_data[1].remove(False)
print (customer_data)

cool = len(customer_data)
print(cool)


cities = ["London", "Paris", "Rome", "Los Angeles", "New York"]
sorted_cities = cities.sort(reverse=True)

print(sorted_cities)

countdown = 10
while countdown >= 0:
  print ("t-minus", countdown)
  countdown -= 1
print ("Blast Off")
'''
countdown = 10
while countdown >= 0:
  print (countdown)
  countdown -= 1

