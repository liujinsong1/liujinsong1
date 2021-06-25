import random
shop=[
    ["机械革命",15000],
    ['mac',20000],
    ["iphone15",10000],
    ['蒙牛酸奶',12],
    ['可口可乐',3],
    ['奶茶',15],
    ['纸抽',1],
    ['辣条',20]
]
money=input('请输入您的钱包余额;')
money=int(money)

mycart=[]

while True:
    A = random.randint(0, 1)
    if A==0:
        print('您抽到的电脑优惠券为：',9,'折')
    else :
        print('您抽到的辣条优惠券为;',3,'折')

    for index,value in enumerate(shop):
        print(index,'',value)

    chose = input('请输入您要买的商品；')
    if str.isdigit(chose):
        chose=int(chose)
        if chose > len(shop)-1 or chose < 0:
            print('您的商品不存在！')
        else:
           if money >= shop[chose][1]:
               mycart.append(shop[chose])
               if A==0 and shop[chose][0]=='机械革命' or shop[chose][0]=='mac':
                   money=money-shop[chose][1]*0.9
               elif A==1 and shop[chose][0]=='辣条':
                   money=money-shop[chose][1]*0.5
               else:
                   money = money - shop[chose][1]
               print('恭喜成功加入购物车，您的余额还剩；', money)
           else:
               print('对不起，您的余额不足，请去其他商城购买！')
    if chose =='q' or chose == 'Q':
        print('欢迎下次光临！')
        break
print('下面是您的购物小票，请拿好')
print(mycart)
print('您的钱包余额还剩',money)







