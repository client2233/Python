target = int(input("请输入目标整数："))

import random
nums = []
for i in range (10000):
    x = random.randrange(1, 65535)
    nums.append(x)
    
isFind = False
n = len(nums)
for i in range(n):
    for j in range(i+1, n):
        if nums[i] + nums[j] == target:
            print([i, j])
            isFind = True

if isFind == False:
    print("找不到！")