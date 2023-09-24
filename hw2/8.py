import random
import math
def pai_1(times):
    sum=0
    for i in range(times):
        x=random.uniform(0,1)
        y=random.uniform(0,1)
        d=1-(x*x+y*y)
        if(d>0):
            sum+=1
    print((4*sum)/times)
print("方法一（蒙特卡罗法）：",end="")
pai_1(1000000)
def pai_2():
    n=6
    a=1
    for i in range(14):
        n=2*n
        a=math.sqrt(2-2*math.sqrt(1-(a/2)**2))
    print(n*a/2)
print("方法二（割圆法）：",end="")
pai_2()
def pai_3():
    pai=16*math.atan(1/5)-4*math.atan(1/239)
    print(pai)
print("方法三（梅钦公式法）：",end="")
pai_3()
