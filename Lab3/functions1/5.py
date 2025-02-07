from itertools import permutations
a = str(input())
def myFunc(a):
  b = permutations(a)
  for i in b:
    print(i)

myFunc(a)