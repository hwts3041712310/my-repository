import random
n=int(input("n:"))
arr=[random.randint(1,10) for i in range(n)]
print(arr)
temp1=arr.copy()
for i in range(1,n):
    temp1[i]=temp1[i]*temp1[i-1]
temp2=arr.copy()
for i in range(n-2,-1,-1):
    temp2[i]=temp2[i]*temp2[i+1]
ans=[0 for i in range(n)]
for i in range(n):
    if i==0:
        ans[i]=temp2[i+1]
    elif i==n-1:
        ans[i]=temp1[i-1]
    else:
        ans[i]=temp1[i-1]*temp2[i+1]
print(ans)
