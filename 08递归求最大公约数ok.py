# 请不要更改源程序的结构，删除原题里的①、②、③、④。填写正确的代码，完善程序。
def gcd(m,n):
    r = m%n
    if r==0:
        return n
    else:
        return gcd(n,r)

a = int(input("请输入一个数："))
b = int(input("请输入另一个数："))
print(a, '和', b, '的最大公约数是：',gcd(a,b))


