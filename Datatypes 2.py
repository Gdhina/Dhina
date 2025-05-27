
# Non-primitive datatypes
# Collection of different primitive datatypes
# n number of methods. maximum set of operations
# list[], tuple(), set{}, dict{} etc(advanced datatypes and datastructures)
# Everything here is mutable(can be changed after declaration) except tuple(immutable)

list1 = [11,3.14,True,"Hello"]
print(list1)


user_list = list(input("Enter elements of a list:"))
print(user_list)

list2 = [1,2,34,5,2,58,42]
print(list2)
# List operations
# left: index starts from zero
# right: index starts from -1
# indexing and slicing method
print(list2[2])
print(list2[-1])
print(list2[4::-1])
print(list2[-1:2:-3])

# append(): element at the last index
list2.append(97)
print(list2)
# insert(index,value): insert element at the speicified index
list2.insert(4,77)
print(list2)
# pop(index): default index is -1
list2.pop()
print(list2)
list2.pop(3)
print(list2)
# remove(value): remove the first occurence
list2.remove(2)
print(list2)
# sort() ascending or descending
list2.sort()
print(list2)
list2.sort(reverse=True)
print(list2)
# reverse() reverse the list
list2.reverse()
print(list2)
# count(value) count the number of occurence of value
print(list2.count(5))
# min and max
print(f"minimum is {min(list2)} and maximum is {max(list2)}")

# any and all
# any: check whether any of the value is True
# all: check whether all the value is True
list3 = [0,0.00," ",False]
print(any(list3))
print(all(list2))
# extend() 
print(list2, list3)
list2.extend(list3)
print(list2)
# copy()
list4 = [] # empty list declaration
list4 = list3.copy()
print(list4)

# Tuples() immutable 
tuple1 = (2,42," ", False)
print(tuple1)

# given a tuple change the values in a tuple
thislist = list(tuple1)
print(thislist)
thislist.append(1000)
tuple1 = tuple(thislist)
print(tuple1)

# set: Collection of unordered pairs
set1 = {1,2,3,4}
print(set1)
set2 ={12,True,73,12,252,52,1}
print(set2)
set2.add("Hello")
print(set2)
set2.remove(12)
print(set2)
set3 = {12,73,764,36,27,32}
set2.difference(set3)
set2.union(set3)
set2.intersection(set3)
set2.clear()
print(set2)

# dictionary : key value pair
dict1 = {'name':'Akil', 'age':23, 'city':'Chennai'}
print(dict1)
print(dict1.keys())
print(dict1.values())
print(dict1.items())
# dictionary methods
dict1['age'] = 28
print(dict1)
print(dict1.get('name'))
print(dict1.get('age'))
dict1.pop('city')
print(dict1)
print(dict1)

d = {'Name': 'Ram', 'Age': '19', 'Country': 'India'}
val = d.popitem() # last value will be removed
print(val)

val = d.popitem()
print(val)

# list of tuples
list_tuples = [(1,23,2),(45,3,53)]
print(list_tuples)
list_dicts = [{'name':'john','age':12},{'name':'jane','age':23}]
print(list_dicts[0].keys())
print(list_dicts[1].get('name'))

# Lambda() function: mathematical expression
# parameters, formula, return value
print(list2)
list2 = list2[:-4] 
# lambda filter function
list4 =[]
list4 = list(filter(lambda x: x%2==0,list2))
print(list4)
print(list1 +list2)
# lambda map function
list3 = [1,35,26,26]
list5 =[]
list5 = list(map(lambda x, y : x+y, list2, list3))
print(list5)