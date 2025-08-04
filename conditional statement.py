# if statement
# -------------------
# if[conditional expression ]:
#       [statement(s) to execute]

a = int(input("enter a value"))
if a % 2 == 0:
    print(a, "Even number ")

# if else statement
# ----------------------
# if[conditional expression]:
#       [statement to execute]
# else:
#        [alternate statement to execute]

a = int(input("enter the value"))
if a % 2 == 0:
    print(a, "even number")
else:
    print(a, "odd number")

# if elif else statement
# --------------------------
# if[condition #1]:
#        [statement #1]
# elif[condition #2]
#         [statement #2]
# elif[condition #3]
#         [statement #3]
# else:   [statement when if and elif(s) are false
per = int(input("Enter the value:-"))
if per >= 68:
    print("first div")
elif per >= 48:
    print("second div")
elif per >= 35:
    print("third div")
else:
    print("faile")
