# Step 1: Create the blueprint using the 'class' keyword
class Car:
    # The __init__ function is the constructor. 
    # It acts like an automated assembly line that sets up your data.
    # 'self' simply means "this specific car we are making right now".
    def __init__(self, brand, color):
        self.brand = brand  # This assigns the brand name to the car
        self.color = color  # This assigns the color to the car

# Step 2: Manufacture real cars (Objects) using our blueprint
car1 = Car("Toyota", "Red")   # Object 1 created
car2 = Car("Honda", "Black")   # Object 2 created

# Step 3: Access data inside the objects
print("--- LU-1: Class & Objects ---")
print(f"Car 1 Brand: {car1.brand}, Color: {car1.color}")
print(f"Car 2 Brand: {car2.brand}, Color: {car2.color}")

