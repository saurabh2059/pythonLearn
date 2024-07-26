file = open( "text.txt", mode="r") 

content = file.read()
print(content)
file.close()

# write

file1 = open("example.txt", mode="w")
file1.write("i am saurabh")
file1.close()


file1 = open("example.txt", mode="w")
file1.write("i am sulavhhh")
file1.close()


# shorter way of opening file dont need to close
with open("example.txt","w") as file2:
    file2.write("hi hi hi hi")

with open("example.txt","a") as file2:
    file2.write(" \t hi hi hi sau")


with open("example.txt", "a") as file3:
    with open("text.txt","r") as file4:
         content = file4.read()
         file3.write(f"\t {content}")
         


with open("text.txt", "r")as file9:
    content2 = file9.readline()


print(content2)



