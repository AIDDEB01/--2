
#introduction to If condition
w1 = 56
w2 = 45
if(w1 > w2):
    print('w2 is lighter than w1')
#Elif condition
w1 = 45
w2 = 54
if w1 > w2:
     print('w2 is lighter than w1')
elif w2 > w1: #try this condition if previous doesnt work
     print('w1 is lighter than w2')
else:
     print('Both are equal')
if w1 > w2: print('w2 is lighter than w1') #short hand
#nested if
if w1 > w2:
     if w1 == 45:
         if w2 == 54:
              print('nested if')

#pass
if(w1 > w2):
     pass

i = 8
while i > 2:
    print(i)
    i -= 1
#example 2
i = 10
while i > 2:
    print(i)
    if i == 5:
        break #OR CONTINUE
i -= 1
#example3
i = 10
while i > 2:
    print(i)
    if i == 5:
        break #OR CONTINUE
    else:
        print('IMPOSSIBLE')
i -= 1
myTuple = ('python', 'c++', 'Java', 'HTML')
for i in myTuple:
    print(i)

for x in 'python':
    print(x)

#Break statement
for i in myTuple:
    if i == 'Java':
        break #or continue
    print(i)

#in range function
for i in range(5): #for i in range(2, 5);
     print(i)

for i in range(3, 50, 5): #increasing by 5 instead of 1
    print(i)
else:
    print("loop ended") 
for i in range(3, 50, 5):
    print(i)
    if i == 48:
        break
else:
    print("loop ended") 

#Nested loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)