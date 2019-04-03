#set
list_1 = [1,2,3,4,5,6,7,8]
list_1 = set(list_1)
print(list_1)
list_2 = set([3,5,7,9])
list_3 = set([3,5,7])

print(list_1,list_2)


#交集
print(list_1.intersection(list_2))
#并集
print(list_1.union(list_2))
#差集difference
print(list_1.difference(list_2))#in list_1 but not in list_2
print(list_2.difference(list_1))#in list_2 but not in list_1
#对称差集
print(list_1.symmetric_difference(list_2))#交集的补集
#集合关系的判断

#判断子集
print(list_1.issubset(list_2))  #list_1是不是list_2的子集
print(list_3.issubset(list_2))
#判断父集
print(list_2.issuperset(list_1))
#判断disjoint
print(list_1.isdisjoint(list_2))#return true if two sets have null intersection


#交、并、差、对称差集的快速写法
print(list_1 & list_2)#交集
print(list_1 | list_2)#并集
print(list_1 - list_2)#差集
print(list_1 ^ list_2)#对称差集


#集合的增删改查
list_1.add(123)     #增
print(list_1)
list_1.remove(123)#删，如果不存在，会报错
print(list_1.pop())#随机删除，删除并且把这个元素返回。无法指定删除
list_1.discard('dddd')#如果集合中没有，不会报错
print(list_1)
print(8 in list_1)#判断在不在里面
print(8 not in list_1)







