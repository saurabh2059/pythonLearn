class Animal:
    def __init__(self,type,age):
        self.type = type
        self.age = age

    def speak(self):
        print(f"{self.type}")


class Dog(Animal):
    def __init__(self, type, age,breed):
        super().__init__(type, age)
        self.breed = breed
   
    def bpeak(self):
         print(f"{self.type}")

    def show (self):
        print(f"{self.type , self.breed , self.age}")

a = Dog("Chaula",2,"german")
a.speak()
a.show()



