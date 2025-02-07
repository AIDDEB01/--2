

def has_33(nums):

    last_num = 0
    for num in nums:
        if last_num == num and num == 3:

            return True
        else:
            last_num = num
    return False


print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))