# list tuple set dist
#

'''# list ->array

list1 = [1,2,3,4,5]

print(list1)
# change the list value
list1[3]=6
print(list1)

# add the item to last
list1.append(6)
print(list1)

# remove the needed item
list1.remove(2)
print(list1)

# give index which u want to pop
list1.pop(0)
print(list1)
'''


# set->undorderd data type with unique values
'''
# big bracket for list , curly for set , small for tuple

set1 ={1,2,3,4,4}
# --> ignores the same value
print(set1)

set1.add(5)
print(set1)
'''

# tuple -> order/unorder doesn't matter

'''a = (1,2,3,4,4)

print(a)'''

# dis-> #value , key

dis = {
    1:"saurabh",
    2:"hello",
    "hello":"main"
}

'''print(dis)

print(dis["hello"])
print(dis[1])'''


for index in dis:
    print(f" {index} holds data : {dis[index]} ")



