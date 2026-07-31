print("future predictior")

name=input("enter your name:")
age=int(input("enter your age:"))
hobby=input("enter your favorite hobby:").lower()

print("\nPrediction")

if age < 18:
    print(name,"you will become great student in the future")

elif hobby == "circket":
    print (name, "you can become a famous circket!")

elif hobby == "gaming":
    print(name, "you can become a successful gamer!")

else:
    print(name, "you will become a very successful person in the fuure!")