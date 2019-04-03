#文件的修改的方式
# 1.将文件加载在内存里，修改完之后然后存回去
# 2.打开一个文件，然后修改完了，写在一个新文件

f = open('大海','r','encoding = utf-8')
f_new = open('大海.bak','w','encoding = utf-8')


for line in f:
    if '慢慢消失的你' in line:
        line = line.replace('慢慢消失的你','慢慢消失的我')
    f_new.write(line)
    f.close()
    f_new.close()
    
