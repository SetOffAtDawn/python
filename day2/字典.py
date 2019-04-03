#字典是无序的
info = {
    '1':'book',
    '2':'bike',
    '3':'computer',
}
#字典的特性：key 唯一，字典是无序的
print(info)

#字典的增、删、改、查


#增
info['4'] = 'bag'



#删
del info
del info['2']

info.pop('2')
info.popitem()#随机删，最好就不要用了


#改
info['1']='desk'


#查
info['3']#可以将其打印出来 print(info['3']),只有在确认字典中有这个才用这种方法，否则没有的话就会出错
print(info.get('4'))#有，就有，如果没有，就会返回none
print('4' in info)#有就true,没有就false

#其他功能
b = {
    1:2,
    3:5,
    '3':'fruit'
}

info.update(b)#将b字典覆盖到info字典上，如果有交叉的部分就更新，如果没有就创建新的。
print(info.items())#将字典转换为列表
c = dict.fromkeys([1,2,3],'test')#初始化一个字典，key为1,2,3.value为test
print(c)

#字典的循环

#只打印key
for i in info:
    print(i)
#同时打印key，value
for i in info:
    print(i,info[i])#最基本的循环，也是最建议使用的循环
#第二种循环
for k,v in info.items():#上面的循环比下面的循环高效很多，这个有把字典转换成列表的过程，如果数据量很大，就浪费时间。
    print(k,v)



#多级字典的嵌套









