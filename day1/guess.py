age_of_oldboy = 56

guess_age = int(input("age:"))

if guess_age == age_of_oldboy:  # if的功能主要是判断
    print("yes,you got it")
elif guess_age > age_of_oldboy:
    print("think smaller!")
else:
    print("think bigger!")






#如果输入不对，要一直猜，直到才对为止
age_of_oldboy = 56



while True:
    guess_age = int(input("age:"))
    if guess_age == age_of_oldboy:  # if的功能主要是判断
        print("yes,you got it")
        break
    elif guess_age > age_of_oldboy:
        print("think smaller!")
    else:
        print("think bigger!")






#限制次数
age_of_oldboy = 56

count = 0

while True:
    if count == 3:
        break
    guess_age = int(input("age:"))
    if guess_age == age_of_oldboy:  # if的功能主要是判断
        print("yes,you got it")
        break
    elif guess_age > age_of_oldboy:
        print("think smaller!")
    else:
        print("think bigger!")
    count +=1


#代码优化
age_of_oldboy = 56

count = 0

while count <3:
    guess_age = int(input("age:"))
    if guess_age == age_of_oldboy:  # if的功能主要是判断
        print("yes,you got it")
        break
    elif guess_age > age_of_oldboy:
        print("think smaller!")
    else:
        print("think bigger!")
    count +=1

#代码优化2
age_of_oldboy = 56

count = 0

while count <3:
    guess_age = int(input("age:"))
    if guess_age == age_of_oldboy:  # if的功能主要是判断
        print("yes,you got it")
        break
    elif guess_age > age_of_oldboy:
        print("think smaller!")
    else:
        print("think bigger!")
    count +=1
else:#if count ==3:
    print("you have tried too many times!")