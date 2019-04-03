#字符串的所有操作
name = "my \tname is alex"

print(name.capitalize())
print(name.count("a"))
print(name.center(50,"-"))#打印50个字符，把name放在中间，如果不够，用-补齐
print(name.endswith("ex"))
print(name.expandtabs(tabsize = 30))#扩展tab键
print(name.find("name"))
print(name[name.find("name"):])
print(name.format(name = "alex",year = 23))
print(name.format_map( {'name':'alex','year':12} ))
print(name.isalnum())#是不是数字或英文字母，如果是特殊字符也会报错
print('abc1234'.isalnum())
print('abcAAAAAB'.isalpha())#是不是字母
print('1a'.isdecimal())#是不是10进制
print('1a'.isdigit())
print('1a'.isidentifier())#是不是一个合法的标识符（变量名）
print('33'.isnumeric())#是不是一个合法的数字，没有什么用
print(''.isspace())#是不是个空格
print('My Name Is '.istitle())#是不是每个首字母大写
print('MY'.isupper())#是不是大写
print(','.join(['1','2','3']))#经常用
print('my name is '.ljust(50,'*'))#确保字符串的长度为50，不够的话用*补上
print('my name is '.rjust(50,'*'))
print('ALEX'.lower())#把大写变成小写
print('alex'.upper())
print('\nalex'.lstrip())#strip默认去掉左右两边的回车和换行和空格，lstrip去掉左边的回车和换行
print('alex\n'.rstrip())
print('      \nalex\n'.strip())
p = str.maketrans('abcdef','123456')#数字和字母是一一对应的
print('alex li'.translate(p))#将’alex li‘中的字母替换成数字

print('alex lil'.replace('1','L',1))#将l替换成L，替换1次
print('alex lil'.rfind('1',))#找到最右面l的下标
print('1+2+3+4'.split("+"))#将字符串根据+号分成列表
print('alex LI'.swapcase())#大写换小写，小写换大写
print('alex,li'.title())#将字符串变成标题模式，首字母大写
print('alex li'.zfill(50))#作用不大，不用记





