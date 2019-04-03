def test(*args):#*代表参数的个数是不固定的 arguments
     print(args)#规范就是*args，不要是其他形式如*joai

test(1,2,3,4,5)
test(*[1,2,3,4,5])#*args = *[1,2,3,4,5]
#args = tuple([1,2,3,4,5])


def test(x,*args):
    print(x)
    print(*args)

test(1,2,3,4,5,6,7)

# **kwargs:将n个关键字参数转换成字典的形式
def test2(**kwargs):#接受字典Keyword Arguments
    print(kwargs)
    print(kwargs['name'])

test2(name = 'mike',age = '8')
test2(**{'name':'mike','age':8})



def test3(name,**kwargs):
    print(name)
    print(kwargs)

test3('mike')
test3('mike',age = 8)

def test4(name,sex,**kwargs):#关键字参数要放到位置参数的后面，放到前面是错误的
    print(name)
    print(kwargs)



def test5(name,age,*args,**kwargs):
    print(name)
    print(age)
    print(args)
    print(kwargs)
