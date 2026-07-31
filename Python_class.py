#step 1:Create the blueprint using the 'class' keyword
class Car:
     # The __init__ function is the constructor.
     # It acts like an automated assembly line that sets up your data.
     # 'self' simply means "this sepecific car we are making rihgt now".
     def __init__(self, brand, color):
           self.brand = brand #this assigns the brand name to the car

           self.color = color #this assigns the color to the car

#step 2:manufacture real cars (object) using our blueprint
car1 = Car("Toyota","Blue")  #object 1 created 
car2 = Car("Honda","Black") #object 2 created

#step 3:acccess data insaide the objects
print("___ LU-1: cclass & objects ___")
print(f"Car 1 Brand: {car1.brand}, Color: {car1.color}")
print(f"Car 2 Brand: {car2.brand}, Color: {car2.color}")