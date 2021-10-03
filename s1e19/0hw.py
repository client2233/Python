nums = []

isInput = True
while isInput == True:
    x = input("请录入一个整数（输入STOP结束）：")
    if x != "STOP":
        nums.append(int(x))
    else:
        isInput = False

target = int(input("请录入目标整数："))

isFind = False
n = len(nums)
for i in range(n):
    for j in range(i+1, n):
        if nums[i] + nums[j] == target:
            print([i, j])
            isFind = True

if isFind == False:
    print("找不到！")