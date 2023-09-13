S=input()
f=0
if(len(S)>0):
    for i in range (len(S)-1):
        if(S[i]==S[i+1]):
            f=1
            break
if(f==0):
    print("no")
else:
    print("yes")
