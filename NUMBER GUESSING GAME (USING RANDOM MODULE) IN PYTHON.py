import random

Cnumber = random.randrange(1, 101)
userInput = int(input("Enter the Number:---"))
if userInput > Cnumber:
    print("Computer Number", Cnumber)
    print("your guess number is too high")
elif Cnumber > userInput:
    print("Computer Number", Cnumber)
    print("your guess number is too low")
else:
    print("computer number", Cnumber)
    print("your guess number is equal")
