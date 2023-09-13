def big(a,b,c):
    if(a>b):
        if(a>c):
            return a
        else:
            return c
    else:
        if(b<c):
            return c
        else:
            return b


x=input()
y=input()
z=input()
print(big(x,y,z))
