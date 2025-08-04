# write a program to check whether person is eligible fo voting or not .

age = int(input("enter your age"))
if age >= 18:
    print("eligible for voting")
else:
    print("not eligible for voting ")

# write a program to check whether a number entered by user  is even odd or even

a = int(input("enter a number"))
if a % 2 == 0:
    print("number is even")
else:
    print("number is odd")

# write a program to check whether a number is divisible by 7 or not

a = int(input("enter a number"))
if a % 7 == 0:
    print("number is divisible")
else:
    print("number is not divisible ")

# write a program to display the last digit of a number (hint: any number %10 will return the last digit)

a = int(input("enter any number"))
print("last digit of number is ,a%10")

# write a program to accept a number from 1 to 7 and display the name of the day like 1 for monday ,2 for sunday and so on..

num = int(input("enter any no between 1 to 7"))
if num == 1:
    print("sunday")
elif num == 2:
    print("monday")
elif num == 3:
    print("tuseday")
elif num == 4:
    print("wednesday")
elif num == 5:
    print("thrusday")
elif num == 6:
    print("friday")
elif num == 7:
    print("saturday")
else:
    print("please enter number between 1 to 7")

# write a program to find the lowest number out of two numbers excepted from user

a = int(input("enter first number"))
b = int(input("enter second number"))
if a > b:
    print("smaller number is:", b)
else:
    print("smaller number is:", a)

# write a program to check a character is vowel or not

ch = input("enter any character")
vow = "aeiouAEIOU"
if ch in vow:
    print("the character is vowel")
else:
    print(" the character is not vowel")
