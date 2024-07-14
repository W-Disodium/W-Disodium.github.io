def fib(n):                      #利用迭代求斐波拉契数列的第n个数
    r1,r2=1,1                    #第1个月、第2个月初值设定
    for i in range(3,n+1):  
        r1,r2=r2,r1+r2
    return r2
month=int(input("输入需要计算的月份数："))
print("兔子总对数为：",fib(month))

        
