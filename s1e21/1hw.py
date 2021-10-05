nums = [2, 2, 4, 2, 3, 6, 2]
    
# 对抗阶段
major = nums[0]
count = 0
for each in nums:
    if count == 0:
        major = each
    if each == major:
        count += 1
    else:
        count -= 1
    
# 统计阶段
if nums.count(major) > len(nums) / 2:
    print("主要元素是：", major)
else:
    print("不存在主要元素。")

