nums = [2, 7, 11, 15]
target = 9

n = len(nums)
for i in range(n):
    for j in range(n):
        if nums[i] + nums[j] == target:
            list = [j, i]

print (list)
            # 将找到的两个元素下标值以列表的形式打印出来 #
