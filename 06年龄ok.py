def age(n):             #递归求年龄
    if n==1:
        return 10
    else:
        return 2+age(n-1)

print("第5个人的年龄是：",age(5)) 
