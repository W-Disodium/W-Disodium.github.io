#请不要更改源程序的结构，删除原题里的①、②、③。填写正确的代码，完善程序
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

n = int(input("输入需要计算的项数："))
print("第", str(n) + "项的值为：", fib(n))
