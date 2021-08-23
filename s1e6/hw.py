
while True:
    point = input("请输入你的分数：")

    if point == 'e':
        break
    else:
        point = int(point)


    if point < 60:
        print("D")
    elif 60 <= point <= 80:
        print("C")
    elif 80 <= point <= 90:
        print("B")
    elif 90 <= point <100:
        print("A")
    elif point == 100:
        print("S")
        