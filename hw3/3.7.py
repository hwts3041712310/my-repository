def deal(a:int,b:int) :
    if b==0:
        return a
    return deal(b,a%b)
[x,y]=[int(i) for i in input().split()]
print(deal(x,y))
