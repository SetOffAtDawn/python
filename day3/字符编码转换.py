# 写文件的时候总是忘记关闭，但是程序执行完之后总会给你关闭
# 如果打开了1000个文件，机器配置不高，电脑就会越来越慢


#with...open...语句,with的作用就是帮你自动关闭文件

with open('大海','r',encoding = 'utf-8') as f:
    pass

#python规范一行不要超过80个字符,所以最好这样写
with open('大海','r',encoding = 'utf-8') as f,\
        open('file','r',encoding = 'utf-8') as f2:
    pass


#字符的编码与转换




