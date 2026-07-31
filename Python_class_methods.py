class Car:
    def __init__ (self, name, color):
        self.name = name
        self.color = color

car1 = Car("Kia", "Blue")
car2 = Car("Honda","Black")

print(car1.name, car1.color)
print(car2.name, car2.color)



    # 1. Class (blueprint)
class students:
    def __init__(self, name1,name2, name3, name4, name5, *marks):
        self.name = [name1, name2, name3, name4, name5]
        self.marks = marks 


# 2. Object (real car)
student1 = students("azan","jebran","maha","sohaib","haris", 50,90,80,70,45)
student2 = students("dua","asma","sara","ali","ahmed", 50,66,44,35,63)

# 3. Use
print(student1.name, student1.marks)
print(student2.name, student2.marks)




class Name:
      def __init__(self, brand, dress,):
          self.brand = brand
          self.dress = dress
      def display(self):
          print("name brand:",self.brand)
          print("name dress:",self.dress)

name1 = Name("j.","blue")
name2 = Name("zelburry","white")

name1.display()
name2.display()


#class(blueprint)
class Car:
    #constructor
    def __init__ (self, color, name):
        #attribute
        self.color = color
        self.name = name
    #object
car1 = Car("Black","Toyota")

#output

print(car1.color, car1.name)