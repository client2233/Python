nums = []

num = input("请输入测试字符串：")

nums.extend(num)

i = 0

while i <= len(nums):
    if nums==[]:
        break

    if nums[i]==')':
        if nums[i-1]=='(':
            nums.pop(i)
            nums.pop(i-1)
            i=0
            continue
        else:
            break
    elif nums[i]==']':
        if nums[i-1]=='[':
            nums.pop(i)
            nums.pop(i-1)
            i=0
            continue
        else:
            break
    elif nums[i]=='}':
        if nums[i-1]=='{':
            nums.pop(i)
            nums.pop(i-1)
            i=0
            continue
        else:
            break
    else:
        i += 1

if nums == []:
    print("合法^o^")
else:
    print("非法T_T")