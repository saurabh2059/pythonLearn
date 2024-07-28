# class and object

'''
    




b =  Student()
print(b.name)


class Person():
    id = 102,
    age = 30



c = Person()


print(c.age)
class Person():
    def __init__(self,id,age):
        self.id = id
        self.age = age

d = Person(103,45)
print(d.age)



for a in range(1,10):
    pass

print("saurabh")

'''


'''   cots obj obj = Student("sau",22,"male")

print(obj.name, obj.age, obj.gender)'''


'''class Student():
    name = "saurabh",
    age = 27,
    gender = "male",

class Student():
    def __init__(self, name ,age , gender):
        self.age = age
        self.name = name
        self.gender = gender
        print("hello from constructor")
class Student():
    roll = 30
    def __init__(self,a,age) :
        self.a = a
        self.age = age

    def roll(self,roll = 22):
        print (f"my roll is {roll}")
        

b = Student("saurabh", 27)
print(b.a)
print(b.age)
print(b.roll(34))'''




class Person():
    id = 102,
    age = 30

class Person():
    
    def __init__(self,id,age):
        self.id = id
        self.age = age
    def ages(self,age = 22):
        print (f"my age is {age}")


abc  = Person(404,33)
print(abc.id)
print(abc.age)
print(abc.ages())



id = int(input("enter the id : "))
age = int(input("enter the age : "))

dec = Person(id,age)

print(dec.id)
print(dec.age)

        