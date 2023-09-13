x=int(input())
y=int(input())
z=int(input())
w=int(input())
l=[x,y,z,w]
l.sort()
for i in range (len(l)):
    print(l[len(l)-i-1])
