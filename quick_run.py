'''
x = [1,2,3,4,5]

new_list = [x*2 for x in x]

print(new_list)

new_list=[]
for x in x:
    change=x*2
    new_list.append(change)

print(new_list)

x = [1,2,3,4,5,6,7,8,9,10]

new_list = [x**2 for x in x]

print(new_list)


x = [3,4,5,6,7,8]

new_list =[x*3 for x in x]

print(new_list)
'''

x = {"type" : "Cat", "lenghth":30}
y = {"material" : "wood", "cost" :30000}

x.update(y)
y.update({"material":"fiber" , "cost":7000})
y.update({"ocean":"atlantic"})
print(y)
