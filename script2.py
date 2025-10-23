'''
new_var1 = "purple"
new_var2 = "black"

print("The new color", new_var1, "and the new color", new_var2, "are really cool")

num1 = 10.3433
num2 = 2.1

print (num1 + num2)

cool1 = (round(num1 + num2,4))

print(cool1)

cool3 = input("Please Enter an number:")

######################


weight = 185

planet = input("Which planet are you on: ").lower()

planet_dic = {"venus": 0.91, "mars": 0.38, "jupiter": 2.34, "saturn": 1.06, "uranus": 0.92, "neptune": 1.19}

if planet in planet_dic:
    weight = weight * planet_dic[planet]
    print ("Your weight is: ", weight)
else:
    print("Your Planet is no where to be found")


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

if x == 0:
  print("x is equal to zero")
elif x >= 0:
  print("x is greater than zero")
else:
  print("x is less than zero")

######################


import random

fortunes = {"cool1", "wow2", "sweet"}
question = input("please end a question")

random_numbers1 = random.randint(0,1)

print ("Magic 8-Ball's answer:", fortunes[random_numbers1])

######################

import random

question = input("What is your question today: ")

fortunes = ["Yes - definitely", "It is decidedly so", "Without a doubt", "Reply hazy, try again", "Ask again later", "Better not tell you now", "My sources say no", "Outlook not so good", "Very doubtful"]

print(len(fortunes))
random_number = random.randint(0, 8)

print ("Magic 8-Ball's answer:", fortunes[random_number])


import random

name = input("What is you name: ")
question = input("What is your question: " )

possible_answers = ["you are cool", "You are super awesome", "You are the best", "You are amazing"]

random_choice = random.randint(0, 3)

print("Hello", name, "my answer to you is",possible_answers[random_choice])

for i in possible_answers:
    print(i)

from dns.rdtypes.util import weighted_processing_order


weight = round(float(input("How much does the package weigh: ")),2)

#Ground Shipping
if weight < 2:
    ground = weight * 1.50
    premium = 125.00
    drone = weight * 4.50
    print(ground, drone, premium)
    if ground < drone and ground < premium:
        print ("I would ship via ground at a price of", ground)
    elif drone < premium:
        print ("I would ship via drone at a price of", drone)
    else:
        print("I would ship via premium at a price of", premium)

if weight > 2 and weight <=6:
    ground = weight * 3.00
    premium = 125.00
    drone = weight * 9.00
    print(ground, drone, premium)
    if ground < drone and ground < premium:
        print ("I would ship via ground at a price of", ground)
    elif drone < premium:
        print ("I would ship via drone at a price of", drone)
    else:
        print("I would ship via premium at a price of", premium)

if weight > 6 and weight<= 10:
    ground = weight * 4.00
    premium = 125.00
    drone = weight * 12.00
    print(ground, drone, premium)
    if ground < drone and ground < premium:
        print ("I would ship via ground at a price of", ground)
    elif drone < premium:
        print ("I would ship via drone at a price of", drone)
    else:
        print("I would ship via premium at a price of", premium)

if weight > 10:
    ground = weight * 4.75
    premium = 125.00
    drone = weight * 14.25
    print(ground, drone, premium)
    if ground < drone and ground < premium:
        print ("I would ship via ground at a price of", ground)
    elif drone < premium:
        print ("I would ship via drone at a price of", drone)
    else:
        print("I would ship via premium at a price of", premium)

for x in range (0,3):
    print(x)



def add (a,b):
    return a+b

b = int(input("input value for b: "))
for a in range (0,3):
    print (add(a, b))


class dog:
    def noise(self):
        return f"the dog goes roof"

    def age(self):
        self.age += 1
        return f"The dogs age is {self.age}"

dog1 = dog.noise("barks loudly")

print(dog1.noise)
print(dog1.age)


'''

x = {"type" : "Cat", "lenghth":30}
y = {"material" : "wood", "cost" :30000}

x.update(y)

y.update({"material":"fiber" , "cost":7000})

y.update({"ocean":"atlantic"})

print(y)

a = [2,3,4,5,6,7]
b = ["cool", "wow", "hot"]

print (a + b)

b[1] = "red"

print(b)

b.append("sea")

print(b)

z = ["red", "blue"]

z.insert(1, "purple")

print(z)

for x in z:
    print(x)

x = 2
y = 1
if x<=5 and y >=5:
    print ("wow")
    print(x)
    x =+ 1
    y =+ 1
elif y>= x:
    print ("y is bigger")
else:
    print("All Bets are off")


def myEmptyFunc():
   # do nothing
   pass
myEmptyFunc()    # nothing happens

my_list = [1,2,4,5,6,7,8]

new_list = [x**2 for x in my_list]

print(new_list)

y = [[1,2,3], [2,3,4], [5,6,7]]

print(y[1][1])

