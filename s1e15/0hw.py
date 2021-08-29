cent = int(input("请输入酒精含量："))

if cent<20:
    print("不构成饮酒行为！")
elif cent<80:
    print("已经达到酒后驾驶的标准！")
else:
    print("已经达到醉酒驾驶的标准！")
