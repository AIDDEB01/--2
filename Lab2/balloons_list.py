"""Booleans"""
print(5 > 3) #True
print(10 > 9) #True
print(10 == 9) #False
print(10 < 9) #False
print(bool("abc")) #True
print(bool(0)) #False

"""Operations"""

"""Arithmetic operations
    // - floor devision
    ** - exponension
    % - modulus
"""
"""Membership(in || not in)"""

"""Identity(is || is not)
    shows if object is exactly the same as another one which means exact equal memory locations"""

""" Bitwise operators
& 	AND	Sets each bit to 1 if both bits are 1	x & y	
|	OR	Sets each bit to 1 if one of two bits is 1	x | y	
^	XOR	Sets each bit to 1 if only one of two bits is 1	x ^ y	
~	NOT	Inverts all the bits	~x	
<<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	x << 2	
>>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	x >> 2
"""

x = 5
x += 3

print (x) #8

print(10*5)
print(10/2)

fruits = ["apple", "banana"]
if "apple" in fruits:
    print("Yes")
if 5 != 10:
    print("five is not equal to ten")
if 5 == 10 or 4==4:
    print("at least one is true")

"""PYTHON LIST"""
#list - allow repitition
thislist = ['a','b','c','a']

print(thislist)
print(len(thislist))

x = list((1,2,3))
print(x)

"""
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
"""

#EX

mylist = ['a','b','c']
print(mylist[1]) #b is answear
mylist = ['a','b','b','c']
print(mylist[2]) #c is answear

#list is changable -> it can be removed

print(len(mylist))

"""Access list items"""

#-1 index means last

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) #3,4,5
#range can be written :5 as only 0,1,2,3,4,5 or :2, alse can be written with negative indexex

mylist = [1,2,3]
print(mylist[-1]) #3 will be printed

fruits = ["apple", "banana", "cherry"]
print(
fruits[1]
)

mylist = ['apple', 'banana', 'cherry', 'orange', 'kiwi']
print(mylist[1:4]) #banana,cherry,orange

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])


"""Change item value"""

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
#list.insert(i, value) method to change 

mylist = ['apple', 'banana', 'cherry']
mylist[0] = 'kiwi'
print(mylist[1]) #banana

fruits = ["apple", "banana", "cherry"]
fruits[0] = 'kiwi'

mylist = ['apple', 'banana', 'cherry']
mylist[1:2] = ['kiwi', 'mango']
print(mylist[2]) #mango

"""ADD list items"""

list.append(value) add value into a list to back 
list.list(value)
list.extend(list_another) add one any object to another to the back

mylist = ['apple', 'banana', 'cherry']
mylist.insert(0, 'orange')
print(mylist[1]) #apple 


fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
fruits = ["apple", "banana", "cherry"]
fruits.insert(1,"lemon")
fruits = ['apple', 'banana', 'cherry']
tropical = ['mango', 'pineapple', 'papaya']
fruits.extend(tropical)

"""remove specific items"""

list.remove(value) only the first occurenc 
list.pop(index) removes specific value, if value index is not typed, removes the last position
del list[index], removes value, if index is not typed, removes full list
list.clear() clear the list
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")

mylist = ['apple', 'banana', 'cherry']
mylist.pop(1)
print(mylist)
#['apple','cherry']

fruits = ['apple', 'banana', 'cherry']
fruits.clear()


"""LOOP LIST"""

list = [1,2,3]
for x in list:
    print(x)

for i in range(len(list)):
    print(list[i])

#What is a correct syntax for looping through the items of a list?
"""for x in ['apple', 'banana', 'cherry']:
  print(x)"""

mylist = ['apple', 'banana', 'cherry']
i = 0
while i < len(mylist):
  print(mylist[i])
  i = i + 1
thislist = [1,2,3]
[print(x) for x in thislist]

"""list comperhension"""

fruits = ['apple', 'banana', 'cherry']
newlist = [x for x in fruits if x == 'banana'] #banana


fruits = ["apple", "banana", "cherry"]
newlist = [x for x in fruits]

fruits = ['apple', 'banana', 'cherry']
newlist = ['apple' for x in fruits]#['apple', 'apple', 'apple']

'''Sort list'''
thislist.sort() #sorts the list in-place alphanumerically
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True) #sort descending, case sensitive, firstly there are capital letters
print(thislist) 
#Customized sort
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc) #Sort the list based on how close the number is to 50
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse() #REverse the order
print(thislist)

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy() #Copy method
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist) #Copy using a list() function
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = thislist[:] #Copy using a slice operator
print(mylist)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2 #Join 2 lists
print(list3)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x) #joining lists using append() function
print(list1)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2) #add items to the end of list1
print(list1)


'''append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list'''
