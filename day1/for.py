#遍历
#从0到9依次遍历
for i in range(10):
    print("loop",i)


#跳一个打一个
for i in range(0,10,2):#默认是1,2代表跳1个，3代表跳2个
    print("loop",i)





#用for循环来写 guess 游戏
age_of_oldboy = 56
for i in range(3):
    guess_age = int(input("age:"))
    if guess_age == age_of_oldboy:  # if的功能主要是判断
        print("yes,you got it")
        break
    elif guess_age > age_of_oldboy:
        print("think smaller!")
    else:
        print("think bigger!")
else:#if count ==3:   else  只有for 循环正常走完才会走这个，如果被break了，就不会走这步了
    print("you have tried too many times!")