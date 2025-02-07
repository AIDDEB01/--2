def has_33(nums): 
 list2 = []
 for i in nums:
  if i not in list2:
   list2.append(i)
 print(list2)
list1 = [int(i) for i in input().split()]
has_33(list1)
