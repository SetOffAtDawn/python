

def fun(x,y):        #x,y为形参，也叫位置参数
    print(x)
    print(y)

fun(1,2)          #1,2为实参，实参和形参一一对应


def test(x,y):
    print(x)
    print(y)

test(x=1,y=2)
test(1,2)
# test(x=1,2)#这种是错误的




'''到目前为止我们所使用的参数都叫做位置参数，因为他们的位置很重要例如一下的使用方式：

def hello_1(name,password)
    print(name+password)
def hello_2(password,name)
    print(password+name)
#这样我们在调用hello方法的时候，必须按照顺序，输入name和password，因为他们的位置比名字更加重要
#上面两个代码所实现的功能是完全一样的，只是参数顺序反过来，使用方式如下
hello_1('name','password')
hello_2('name','password')
#以上两个调用结果输出都是 “namepassword”

但是如果参数很多的时候，我们在调用时可能很难记住参数的顺序，我们引入关键字参数即使用参数名提供的参数，在于明确每个参数的作用，使得函数调用的时候，参数的含义变得更加清晰

#以前面的hello_1函数为例
hello_1(name='name',password='password')
hello_1(password='password',name='name')
#以上两种写法输出结果都是“namepassword”
#这样我们在调用时，顺序就完全没有影响了，不过要注意参数名和值一定要对应

而且关键字参数可以在定义函数的时候提供默认值

def hello_3(name='name',password='password')
    print(name+password)
#参数具有默认值的时候，调用的时刻可以不用提供参数，可以不提供、提供一些或提供所有的参数
hello_3()#输出“namespace”
hello_3('username')#输出“usernamepassword”
hello_3('username','pwd')#输出“usernamepwd”
#如果只想提供password的参数，而让name使用默认值，使用方法如下
hello_3(password='pwd')#输出“namepwd”

位置参数和关键字参数可以联合使用，但是要注意位置参数需要放置在关键字参数前面，例如

def hello_4(hel,name='name',password='password')

'''