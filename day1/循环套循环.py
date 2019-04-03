

#大循环一次，然后小循环10次
for i in range(10):
    print("--------",i)
    for j in range(10):
        print(j)





for i in range(10):
    print("--------",i)
    for j in range(10):
        print(j)
        if j > 5:
            break     #break 跳出本次循环，小循环