a=int(input())
if(a==1):
    print(1)
elif(a==2):
    print(2)
else:
    if(a%3==0):
        for i in range(a//3):
            print(3,end=" ")
    elif(a%3==1):
        print("2 2",end=" ")
        for i in range(1,a//3):
            print(3,end=" ")
    else:
        print(2,end=" ")
        for i in range(a//3):
            print(3,end=" ")
