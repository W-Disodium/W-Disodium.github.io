def hanno(n,a,b,c):
    #定义一个函数，将n个木盘从a借助b移动到c
    if n==1:
        print(a,'-->',c)
    else:
        hanno(n-1,a,c,b)
        print(a,'-->',c)
        hanno(n-1,b,a,c)
    
#主程序：调用hanno自定义函数，实现num个盘子从'A'借助于'B'移动到'C'
num=int(input("请输入木盘的个数："))
hanno(num,'A','B','C')


