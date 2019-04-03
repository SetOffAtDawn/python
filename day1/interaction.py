

#用户输入

username = input("username:")  #input默认输入的是字符串
password = input("password:")
print(username,password)



#格式化输出

name = input("name:")
age = input("age:")
job = input("job:")
salary = input("salary:")

info ='''
------ info of  %s------
Name:%s
Age:%s
Job:%s
Salary:%s
'''%(name,name,age,job,salary)
print(info)
#   %s代表字符串 string
#   #d代表数据   digital
#   #f代表数据   float







name = input("name:")
age = int(input("age:"))  #int  指的是interger 整型
job = input("job:")
salary = input("salary:")

info ='''
------ info of  %s------
Name:%s
Age:%d
Job:%s
Salary:%s
'''%(name,name,age,job,salary)
print(info)

