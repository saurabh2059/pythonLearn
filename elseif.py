# WAP to check if the given user is  inbetween 18 and 59  print he can vote if user is abive 60 and show too old if below 18 show too young

age = int(input("enter the age of person  (greater than 0):"))

if age>=18 and age<=59:
    print("user can vote")
    # & can also be used
elif age<18:
    print("user is too young")
elif age>60:
    print("user is too old")
else:
    print("invalid age number")

print("\n\n")
# wap to check the day using if else elif
day = input("enter the day (small case): ")

if day == "sunday":
    print("this is 1st day of week . its sunday today")
elif day == "monday":
    print(" this is 2nd day of week monday")
elif day == "tuesday":
    print(" this is 3rd day of week tuesday")
elif day == "wednesday":
    print(" this is 4th day of week wednesat")
elif day == "thursday":
    print(" this is 5th day of week thursday")
elif day == "friday":
    print(" this is 6th day of week friday")
elif day == "saturday":
    print(" this is 7th day of week sarturday")
else:
    print("you fool")


print("\n\n")
#wap to check if user can drink or not
if age>=18 :
    print("user can drink")
    # & can also be used
elif age<18:
    print("user is too young cant drink")


