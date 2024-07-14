x=int(input('请输入任一正整数：'))
n=0
while(x!=1):
    if(x%2!=0):
        x=x*3+1
    else:
        x=x//2
    print(x ,end=' ')
    n=n+1 
print()
print('总步数：',n)
