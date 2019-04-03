#自己写模块
import getpass

_username = "alex"
_password = "123"

username = input("username:")
password = getpass.getpass("password:")

if _username == username and _password == password:
    print("welcome user {name} login...".format(name=username))
else:
    print("Invalid username or password!")
#写完这个模块之后，就可以用Import进行导入了，默认导入是先在当前目录下寻找模块，
#如果在此目录下没有找到，就会在全局变量中寻找模块，再找不到就会报错