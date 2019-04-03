
'''
open("file")#这已经将文件打开了，只是你没有看到而已

# data = open('file',encoding= 'utf-8').read()#这个是打开之后，读一下，并没有将这个
#打开的文件赋予一个对象，所以打开之后，读一下就消失了
# 最好的方法，读
f = open('file',encoding='utf-8')#文件句柄
data = f.read()#这种操作方法是将上面的一步分成两步

print(data)

'''
# 写
f = open('file2','w',encoding='utf-8')#w是先创建一个文件，然后再往里写东西
# 如果打开已有的文件，用w会创建一个新文件，然后覆盖之前的文件，这很危险。
f.write('我爱北京天安门\n')
f.write('天安门上太阳升')

#追加
f = open('file2','a',encoding='utf-8')
f.append('\n我爱北京天安门。。。。')
# append 模式也不能读
# f.read()会报错


#怎么读前五行
# 不是print(f.readline())写五次
for i in range(5):
    print(f.readline())


for line in f.readlines():#f.readlines()是将文件变成列表的形式
    print(line)
#或者
for line in f.readlines():
    print(line.strip())#这个是去掉空行和换行
#比较一下上面两个循环，一个不打印i，另一个打印line

#一行一行的读，效率最高，只保存一行
for line in f:
    print(line)



#文件的其他用法
f.open('file','r',encoding='utf-8')
print(f.tell())#告诉你打印出来的字符数量
print(f.readline())
print(f.tell())


print(f.read(5))
print(f.tell())
f.seek(0)#将打印的光标回到某处、0位最初的起点
print(f.readline())#重新开始打印第一行
f.seek(10)
print(f.readline())#会从第一行的第10个字符串的位置打印到一行的末尾


#
print(f.encoding)#打印文件的编码

#
print(f.fileno())#打印python调用操作系统的编号
print(f.name)#打印文件名
print(f.isatty() )#打印是否是终端设备
print(f.flush())#强制将存在缓存的内容存到硬盘上


#
f.truncate()#什么都不写就会将文件清空
f.truncate(10)#从开头开始截断

f.seek(10)
f.truncate(20)#移动没有用，还是从开头开始截断

#既能读又能写
f = open('file','r+',encoding='utf-8')
# r+读写
f.readline()
f.readline()
f.write('------------')#无论怎么读，都是从最后一行开始写

f = open('file3','w+','encoding=utf-8')
# w+写读，几乎没有什么用
f.write('-------0-------\n')
f.write('-------0-------\n')
f.write('-------0-------\n')
print(f.tell())#打印位置
f.seek(10)#回到第十个位置
print(f.readline())
f.write('111111111')
f.close()
# 打开文件，如果修改的话，之前的内容会被覆盖
# 在哪个位置写，哪个位置的内容会被覆盖
# a+，追加，读
# rb,以二进制方式读，read binary
f = open('file','rb')
#以rb方式读的时候不要加encoding，都是二进制了，就没有编码模式了
# 网络传输只能用二进制模式

f = open('file','wb')#wb，写二进制文件
f.write('hello binary'.encode())
f.close()









