import random
import math
def fixedIntegrals(times):
    sum=0
    for i in range(times):
        x=random.uniform(2,3)
        y=random.uniform(0,21)
        d=(x*x+4*x*math.sin(x))-y
        if(d>0):
            sum+=1
    print((21*sum)/times)
times=int(input("请输入times:"))
fixedIntegrals(times)

    
