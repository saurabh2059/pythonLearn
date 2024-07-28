# a = [1,2,3,4]
# print( len(a))

# name = "saurabh"

# print ( len (name ))

# for i in range( len(name)):
#  print (name[i])

#  function definitiion

'''def a():
    print("\n welcome to the heaven \n")

a()
a()

def g():
    return 5+6

print( g())

def h(i,j,k):
    print( i+j+k)


h(5,5,6)'''

#  wap that takes input ffrom user calss name and print as a function paramenter 

#  wap that add 4 values in from the function parameter

'''def name(a):
    print(f" hello , {a}")

def adder(b):
    print(b+4)

name("saurabh")
adder(9)'''

'''def factorial(n):
    if(n==1):
        return 1
    else:
        return n*factorial(n-1)



s= factorial(5)

print(s)
'''
# function parameter type

# named , default , *args , 

'''def p (name = "saurabh"):
    print(name)



p()
p("sugam")'''

'''def r(name,age):
    print(f"{name} and my age is {age}")

r("saurabh",22)


def r(name,age,*args):
    print(f"{name} and my age is {age},{args}")

r("saurabh",22,3,3,4,5)
# keyword parameter
def s(name,age):
    print(f"name:{name} and age:{age}")

s(age = 27 , name = "saurabh")'''


def hi(*names):
    for name in names:
        print(f"name is {name}")

hi("saurabh","sulav","aashish","madhav")


# creating param and val in the main calling function
def t(**val):
    print(val)

t(name = "saurabh", age=22)