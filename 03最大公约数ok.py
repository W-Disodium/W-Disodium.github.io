m=int(input('请输入正整数m：'))
n=int(input('请输入正整数n：'))
r=m%n
while r!=0:
    m=n
    n=r
    r=m%n
print('最大公约数是：',n) 

