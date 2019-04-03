#获取密码

import getpass

username = input("username:")
password = getpass.getpass("password:")

print(username,password)


#pycharm 中不好用，得在都是界面好用


#判断密码是否正确

import getpass

_username = "alex"
_password = "123"

username = input("username:")
password = getpass.getpass("password:")

if _username == username and _password == password:
    print("welcome user {name} login...".format(name=username))
else:
    print("Invalid username or password!")




