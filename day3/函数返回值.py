def test1():
    print('test1')

def test2():
    print('test2')
    return 0

def test3():
    print('test3')
    return 0,'hello',['sdfa','fasdf']

x = test1()
y = test2()
z = test3()
print(x,y,z)
# 返回这三个东西：none，值，对象