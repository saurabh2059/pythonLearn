class Person():
    name = "saurabh"

    def __init__(self,name,age,location):
        self.name = name 
        self.age = age 
        self.location = location 
    
    def names(self):
        return self.name

    @classmethod
    def names(cls):
        return f"{cls.name}"
    def ages(cls):
        return f"{cls.age}"
    
    @staticmethod
    def add(a,b):
        print(a+b)


b = Person("Shishir", 22 , "ktm")
# print(b.names())

print(Person.names())
print(b.age)
print(b.location)

# Person.add(4,5)

Person.add(7,5)




