#存名字

names= "zhangyang guyun xiangpeng xuliangchen"
#不好读，不好改

#列表
names = []
print(names)


#读、增、删、改、查
#读取信息,列表的打印
names = ["zhangyang","guyun","xiangpeng","xuliangchen"]
print(names[0])
print(names[0],names[1])
print(names[0:2])#  切片  起始位置包括，结束位置不包括。助记：顾头不顾尾
print(names[-1])#取倒数第一个值，从右开始数
print(names[-1:-3])#错误案例
print(names[-3:-1])
print(names[-3:])#能取到最后面的值
print(names[0:3])
print(names[:3])#前面有0的话，可以省略
print(names[0:-2])#这里的-2是从右往左数两个


#增加信息
names = ["zhangyang","guyun","xiangpeng","xuliangchen"]
names2 = [1,2,3,4]
names.append("leihaidong")
names.insert(1,"chenronghua")#插在guyun前面
names.extend(names2)#names2 仍然存在


#删除信息
names = ["zhangyang","guyun","xiangpeng","xuliangchen"]
names.remove("guyun")
del names[1]
names.pop()#默认删除最后一个，输入下标删除某一个值

#更改信息
names = ["zhangyang","guyun","xiangpeng","xuliangchen"]
names[2] = "xiedi"

#查询信息
names = ["zhangyang","guyun","xiangpeng","xuliangchen"]
print(names.index("guyun"))
print(names[names.index("guyun")])

#统计数量
names = ["zhangyang","guyun","guyun""xiangpeng","xuliangchen"]
print(names.count("guyun"))

#清除列表
names = ["#zhangyang","4guyun","guyun""xiangpeng","xuliangchen"]
names.clear()
names.reverse()#反转
names.sort()#排序，根据ASCLL码排序规则进行排序  特殊符号，数字，大写，小写

#列表的复制
names = ["#zhangyang","4guyun","guyun""xiangpeng","xuliangchen"]
names2 = names.copy()
names[2] = "顾云"
print(names,names2)    #names2不变


#列表套列表
names = ["#zhangyang","4guyun",["alex","jack"],"guyun""xiangpeng","xuliangchen"]
#此列表中的列表只是内存地址
names2 = names.copy()#此copy为浅copy,只会复制第一层列表，不会复制第二层列表，
#copy的列表只是copy了内存地址
names[3] = "顾云"
names[2][0] = "ALEX"
print(names,names2)#此时出现的结果是names,names2中的"alex"都会变成"ALEX"


#浅copy再补充
import copy

'''浅copy实现的三种方式
person = ["name",["saving",1000]]
p1= copy.copy(person)
p2= person[:]
p3=list(person)
'''
p1 = person[:]
p2 = person[:]

p1[0] = "alex"
p2[0] = "wife"
p1[1][1]=50
print(p1)  #目的：用来创造联合账号








#深copy
import copy
names = ["#zhangyang","4guyun",["alex","jack"],"guyun""xiangpeng","xuliangchen"]
names2 = names.deepcopy(names)
names[3] = "顾云"
names[2][0] = "ALEX"
print(names,names2)


#列表的循环
names = ["#zhangyang","4guyun",["alex","jack"],"guyun""xiangpeng","xuliangchen"]
for i in names:
    print(i)
#列表的跳跃打印
names = ["#zhangyang","4guyun",["alex","jack"],"guyun""xiangpeng","xuliangchen"]
print(names[0:-1,2])
print(names[:-1,2])






