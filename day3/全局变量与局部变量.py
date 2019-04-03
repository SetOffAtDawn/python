def changge_name():
    global name    #将此变量名变成全局变量
    name = 'mike'

changge_name()
print(name)

# 这种方式不要用，出错之后相当麻烦，作死行为，用了就被开除
