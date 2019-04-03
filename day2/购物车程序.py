#需求：启动程序后让用户输入工资，然后打印商品列表
#     允许用户根据商品编号购买商品
#      用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒
#     可随时退出，退出时，打印已购买的商品和余额

product_list = [
    ('iphone',5800),
    ('computer',12000),
    ('book',100),
    ('coffee',30),
]
#每进行一部的时候，想一想要不要进行判断和循环
#步骤解析：
#首先让用户输入商品
#然后判断用户输入的是不是数字，如果是数字，打印商品列表和序号；如果不是返回错误提示
#让用户选择需要买的商品的序号
#判断用户的钱能否够，如果够，购物车加上这个商品，并且显示用户的余额
#重复上述步骤
#步骤解析：

shoppping_cart = []
salary = input('Please input your salary:')

if salary.isdigit():
    salary = int(salary)
    while True:
        for i in product_list:
            print(product_list.index(i),i)
        choice = input("请输入你选择的商品序号：")
        if choice.isdigit():
            choice = int(choice)
            if choice <len(product_list) and choice >=0:
                p_item = product_list[choice]
                if p_item[1] <=salary:
                    shoppping_cart.append(p_item)
                    salary -= p_item[1]
                    print('%s商品已放入购物车，您的余额还有%s'%(p_item,salary))
                else:
                    print('您的余额不足！')
            else:
                print('您输入的数字有误！')

        elif choice == 'q':
            print('--------shopping_cart---------')
            for p in shoppping_cart:
                print(p)
            print('您的余额为：',salary)
            #不必要这样写print('您的余额为：%S',salary),当有多个需要替代的值时，才这样写。
            exit()#退出整个程序
        else:
            print('您输入有误！')
else:
    print('您输入的金额有误')

