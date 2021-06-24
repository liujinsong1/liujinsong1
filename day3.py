import random
data=random.randint(0,200)
coin=5000
i=0
print(data)
while i<=10:
    num=input("请输入您要输的数字：")
    num=int(num)
    if num>data:
        coin = coin - 500
        print("大了,您的当前金额为：",coin,"您的一共用了次数为；",i+1,"次")
    elif num<data:
        coin = coin - 500
        print("小了,您的当前金额为：",coin,"您的一共用了次数为；",i+1,"次")
    else:
        print("恭喜您猜中了，本次答案为:",num,",您当前的余额为；",coin,"您的一共用了次数为；",i+1,"次")
        coin=coin+1000
        break
    i=i+1


