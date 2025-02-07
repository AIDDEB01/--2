def spy_game(nums):

    last_num = 1
    last_last_num = 1
    for num in nums:
        if last_num == last_last_num and num == 7 and last_num == 0:

            return True
        else:
            last_last_num = last_num
            last_num = num
    return False

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))