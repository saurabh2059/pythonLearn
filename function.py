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

def name(a):
    print(f" hello , {a}")

def adder(b):
    print(b+4)

name("saurabh")
adder(9)

def factorial(n):
    if(n==1):
        return 1
    else:
        return n*factorial(n-1)



s= factorial(5)

print(s)


