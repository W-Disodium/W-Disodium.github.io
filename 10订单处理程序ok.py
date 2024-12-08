listque=[]                        #定义listque存储订单
x=0
while x!=4:                      
    print('1. 添加订单')
    print('2. 发货')
    print('3. 查看订单列表')
    print('4. 退出')
    x=int(input("输入你的选择:"))     #输入选择项
    if x==1:
        y=input("输入订单编号:")  #输入订单编号
        listque.append(y)                        #在listque中添加订单号
    elif x==2:
        if len(listque)==0: 
            print("所有订单均已发货")
        else:
            print("发货单号:" , listque.pop(0))
    elif x==3:
        print("等待发货:",listque)
    print() 
input("运行完毕，请按回车键退出...")
