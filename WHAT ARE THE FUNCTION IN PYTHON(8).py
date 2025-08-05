# USER DEFINED FUNCTION:-

#  A function is block of statement which can be used repetitively in program.
#  it saves the time of developer In python concept of function is same as in other langauge.
#  You can pass data ,know as parameter, into a function.

# CREATING A FUNCTION :-

# IN python a function is defined using the (def keyword).
#  def showdata():
#     print("welcome to matalbiduniya").

# CALLING FUNCTION:-

#    showdata()
#  output:-welcome to matalbiduniya

def showdata():
    print("welcome to matalbiduniya")


showdata()
showdata()
showdata()
showdata()

# FUNCTION ARGUMENTS:--

# information can be passed to function as parameter
#  def sum(a,b)
#      print(a+b)

# CALLING WITH ARGUMENT
#  sum (sum20,10)
#  output:30

print()


def sum(a, b):
    print(a + b)


sum(20, 10)
sum(40, 20)
sum(30,67)
print()


# DEFAULT PARAMETER VALUE

# def sum(a,b=1):
#     print(a+b)

# calling with arguments
# sum(20)
# output:- 21
# sum(20,10)
# output:-30

def sum(a, b=30):
    print(a + b)


sum(20)
sum(40, 20)

print()


# RETURN VAlUES

# to let a function return a value use the return statement:

# def square(x):
#      return x*x
# s=square(5)
# output:25

def square(x):
    return x * x, x * 4


s = square(5)
print(s)
