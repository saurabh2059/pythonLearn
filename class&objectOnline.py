class Person :
    name = "saurabh"
    age = 22
    occupation = "student"

    def __init__(self,name,age,occupation):
        self.name = name
        self.age = age
        self.occupation = occupation
   
  

    def details(self):
        sau = input("\n enter your name : ")
        ary = int (input("\n enter your age : "))
        al = input("\n enter your occupation : ")
        self.name = sau
        self.age = ary
        self.occupation = al
       

    def disp(self):
        print(f" \n\n{self.name} is a {self.occupation}")



xyz =Person("sulav",15,"student")


xyz.disp()
xyz.details()
xyz.disp()



