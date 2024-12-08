#定义加密函数，对字母进行加密，即向后移动3位，其他字符不加密。
def ks_jiam(befmessage):   
    aftermessage=""
    for char in befmessage:
        if "A"<=char<="W" or "a"<=char<="w":
            aftermessage=aftermessage+chr(ord(char)+3)
        elif "X"<=char<="Z" or "x"<=char<="z":
            aftermessage=aftermessage+chr(ord(char)-26+3)
        else:
            aftermessage=aftermessage+char
    return aftermessage
#以下为主程序
yuanwen=input("请输入原文：")
print(ks_jiam(yuanwen))

