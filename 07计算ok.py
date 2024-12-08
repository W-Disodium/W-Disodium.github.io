def jc(n):    #利用递归的方法求n！
    if n == 0 or n==1:   
        return 1  
    else:
        return n*jc(n-1)   

n=int(input('请输入正整数n：'))
if n>0:   #如果n为正数，且为整数
    A = 3**n/jc(n)     #计算A的值
    print('A=', A)
else:
    print('输入的数据有误，无法计算')
