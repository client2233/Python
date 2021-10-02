num = int(input("请输入一个正整数："))
num1 = 0
for each in range(0, num, -1):
    num1 = num1*10 + num

if num == num1:
    print("是回文数")