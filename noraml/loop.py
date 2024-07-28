'''  for i in range(10):
     print(i)
 '''

'''
a = [1,2,3,4,5]
for i in a:
    print (i)
'''
# v = 10
# while(v > 0 ):
#     print(v)
#     v-=1

'''
num = int(input("enter a number : "))

for j in range(10):
        print(f" \t {num} * {j+1}: {num*(j+1)}")
   
for j in range(1,11):
        print(f" \t {num} * {j}: {num*j}")
'''


# nested loop 
'''
for j in range(1,11):
        print( "\n ",j)
        for i  in range(1,11):
                print(f"{j} * {i} = {j*i}")
'''


'''
first = int(input("enter a 1st  number : "))
second = int(input("enter a 2nd  number : "))

for i in range (first, (second+1)):
    print( "\n ", i)
    for j in range(1,11):
        print(f"{i} * {j} = {j*i}")

'''

# break
'''
for i in range(10):
    if i ==5:
        break
    else:
        print(i)

'''


# continue
'''
for i in range(10):
    if i ==5:
        continue
    else:
        print(i)
'''




