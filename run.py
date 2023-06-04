import math

num=input("数字!次方根:")
num=num.split("!")
num,m=float(num[0]),float(num[1])
n = 0.1
a = 1
while a**m!=num: # 设置一个误差范围，避免无限循环
    if (a+n)**m > num > a**m:
        n = n/10
        print(a,a**m,n)
        if (a+n)**m<=num:
            a = a+n
        print(a,a**m,n,"on")
    else:
        if (a+n)**m<=num:
            a = a+n
        print(a,a**m,n,"on")
        
a = math.exp(math.log(num)/m) # 使用math模块来计算a的值

print(a,a**m,"off") # 使用格式化字符串来控制输出的精度
