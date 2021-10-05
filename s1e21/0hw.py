list = [2,2,4,2,3,6,2]

list.sort

n = list[len(list)//2]

j = 0

for i in range(len(list)):
    if list[i]==n:
        j += 1

if j>=len(list)//2:
    print (n)
else:
    print ("no!")