n=float(input())
a=0
def find(n):
    if(n<0):
        a=0-n
    l=0
    r=a
    m=(l+r)/2
    while(abs(m*m*m-a)>0.000001):
        if(m*m*m>a):
            r=m
        else:
            l=m
        m = (l + r) / 2
    if(n<0):
        m=0-m
    print('%.3f'%m)
find(n)



