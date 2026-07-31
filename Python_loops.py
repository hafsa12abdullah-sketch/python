#simple loops
for i in range (5): 
    print (i)


for i in range(1,11):
    print(i)


#loop with break
for i in range(10):
    if i == 8:
        break
    print(i)

#loop with continue
for i in range (10):
    if i == 2:
        continue
print(i)


#simple loop
for j in range(0,11):
    print(j)

#lopp with dictonary
my_dict = {
    "name": "Ali",
    "age": 20,
    "city": "Karachi"
}

for key, value in my_dict.items():
    print(key, value)

#nested loop
for i in range (6):
    for j in range(5):
        print(i,j)


#loop with dictonary
students = {
    "name":["maha","neha","iqra","ayehsa","aliza"],
    "marks":[80,55,65,73,45],
    "city":["karachi","islamabad","korangi","panjab","lahore"],
    "age":[30,22,15,23,20]
}
for value in students.values():
    print(value)



#loop with dictonary
students = {
    "name":["maha","neha","iqra","ayehsa","aliza"],
    "marks":[80,55,65,73,45],
    "city":["karachi","islamabad","korangi","panjab","lahore"],
    "age":[30,22,15,23,20]
}
for key in students.keys():
    print(key)


#loop with dictonary
students = {
    "name":["maha","neha","iqra","ayehsa","aliza"],
    "marks":[80,55,65,73,45],
    "city":["karachi","islamabad","korangi","panjab","lahore"],
    "age":[30,22,15,23,20]
}
for key, value in students.items():
    print(key, value)


#loop with list

for color in ["blue","white","grey","ice blue","black","green"]:

    print(color)

