class dress:
    def __init__ (self, brand, color):
        self.brand = brand
        self.color = color
        
    def show(self):
        print(self.brand, "salitex")    
        
dress1 = dress ("salitex","mint green")

print (dress1. brand)
print (dress1. color)

dress1 .show()  




class Student:
    def __init__(self, name):
        self.name = name
        
    def show(self):
        print(self.name)
            
s1 = Student ("Dua")
s2 = Student ("Zara") 

s1.show()
s2.show()  




class students :
    def __init__(self, name):
        self.name = name
        
    def display(self):
        print("name:" ,self .name)
        
s1 = students ("ali")
s1.display()



#CLASS 
class student:
    pass


#OBJECT 
class student:
    pass
s1 = student
print(s1)


#CONSTRUCTOR __init__:
class student:
    def __init__(self):
        print("constructor called")
        
s1 = students 



class Students:
    def __init__(self, name ,age):
        self.name = name
        self.age = age
        
s1 = Students ('zara',25)
       
print(s1.name)
print(s1.age)

      

class Student:
    def __init__(self,name, age):
        self.name = name   
        self.age = age 
        
    def display(self):
        print("name:", self.name)
        print("age:", self.age)
        
student1 = Student("ali",15)

student1.display()      



class Car:
    def __init__(self, brand ,color):
        self.brand = brand
        self.color = color
        
    def start (self):
        print(self.brand,"car is starting")
        
car1 = Car("Toyota","Black")

print(car1.brand)
print(car1.color)

car1.start()





      
class ClassName:

    def __init__(self, students, marks):
        self.students = students
        self.marks = marks

    def show(self):
        print(self.students)
        print(self.marks)


#object_name 
s1 = ClassName(["ali","zara","dua","hasan","gul"], [45,67,80,35,44])

#object_name
s1.show()     




class Students:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def show(self):
        print(self.name , self.marks)
        
s1 = Students("zara",35)
s2 = Students("sara",50)

s1.show()
s2.show()             
        
            

class Brand:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        
    def display(self):
        print(self.name , self.color)
        
s1 = Brand("zellbury","blue")
s2 = Brand("saya","white")
s3 = Brand("salitax","mint green")
s4 = Brand("khaadi","orange")


s1.display()                    
s2.display()
s3.display()        
s4.display() 



class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

# Object
s1 = Student("Zara", 50)

# Direct Access
print("Name:", s1.name)
print("Marks:", s1.marks)             
            
            
            
class Marks:
    def __init__(self, students , marks):
        self.students = students
        self.marks = marks
        
    def show (self):
        print(self.students, self.marks)
        
s1 = Marks ("maha",60)
s1 . show()     
                  
                  

                  
class Car:
    def __init__(self, name):
        self.name = name
    
    def show (self):
        print(self.name)
        
s1 = Car ("kia")
s1 . show()                                
        

class Institute:
       
    def show(self):    
        print("i teach python in ecti")
        
s1 = Institute()
s1 . show()                



class name:
    def __init__(self,car,brand):
        self.car = car
        self.brand = brand
        
        
    def show(self):
        print(self.car, self.brand)
        
c1 = name ("toyota","kia")
c1 . show ()


class Brand:
    def __init__(self, name,color):
        self.name = name
        self.color = color 
        
    def display(self):
        print(self.name,self.color)
        
b1 = Brand ("zellbury","ice blue")
b1 . display()        



class Cars:
    def __init__(self,name,brand,color):
        self.name = name
        self.brand = brand
        self.color = color
        
    def show(self):
        print(self.name,self.brand,self.color)
        
c1 = Cars("Corolla","toyota","blue")
c2 = Cars("Kia Sportage","kia","black")
c2 = Cars("Alto","Suzuki","olive green")    
c3 = Cars("Cultus","Suzuki","gry")

c1 . show()
c2 . show()
c3 . show()



class ClothingBrand:
    def __init__(self, fabricname,brand,color):
        self.fabricname = fabricname
        self.brand = brand
        self.color = color
        
    def display(self):
        print(self.fabricname,self.brand,self.color)
        
        
c1 = ClothingBrand("LAWN","SAYA","BLUE")
c2 = ClothingBrand("KARANDI","KHADDI","RUST")
c3 = ClothingBrand("KHADAR","ALKARAM","PURPLE")
c4 = ClothingBrand("LINEN","NISHAT","GRY")
c5 = ClothingBrand("ORGANZA","MUSHK","OFF WHITE")
c6 = ClothingBrand("CHIFFON","ASIM JOFA","ICE BLUE")
c7 = ClothingBrand("SILK","MARIA B","MEHROON")
c8 = ClothingBrand("CHIKANKARI","GULJEE","LILAC&MINTGREEN")
c9 = ClothingBrand("CRUSHFABRIC","SALITAX","YELLOW")
c10 = ClothingBrand("RAW SILK","LAKHANI","PINK")

c1 . display()            
c2 . display()   
c3 . display() 
c4 . display()              
c5 . display() 
c6 . display() 
c7 . display() 
c8 . display() 
c9 . display() 
c10 . display() 


