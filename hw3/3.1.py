n=float(input())
a=int(n)
b=n-a
ans=""
while a:
    ans=str(a%2)+ans
    a//=2
if b:
    ans+='.'
    i=99999
    while b and i:
        b*=2
        if b>=1:
            ans=ans+'1'
            b-=1
        else:  
            ans=ans+'0'
        i-=1
print(ans)
