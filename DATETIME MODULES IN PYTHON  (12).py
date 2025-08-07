# import a module named datetime to work with dates as data objects.

# IMPORT DATETIME
# (X = datetime.datetime.now())
# print()  the data contain year,month,day,hour,minute,second,and microsecond.

# CREATING DATA OBJECTS
# x=datetime.datetime(2021,1,18)
# print()

import datetime

x = datetime.datetime.now()
print(x)

print(datetime.datetime(2022, 2, 22))

# he method is called strftime(),and takes one parameter,format, to specify the format of the returned string:

# %b month name, short version - Dec
# %B month name, full version  - December
# %m month as a number 01-12    - 12
# %y year,short version,without century -18
# %Y year,full version - 2018
# %H Hour 00-23        -17
# %I Hour 00-12        -05
# %p AM/PM             -PM
# %M minute 00-59      -41

# IMPORT DATETIME

# now=datatime.datetime.now ()#current data and time
# year=now.strftime("%Y")
# print("year:",year)

import datetime

x=datetime.datetime.now()
m=x.strftime("%I")
print(x)
print(m)

print(datetime.datetime(2022,2,22))