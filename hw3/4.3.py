import random
def sort(list):
    for i in range (len(list)):
        now=i
        n=list[i]
        while now-1>=0 and list[now-1]>n:
            list[now]=list[now-1]
            now-=1
        list[now]=n
    return list
list=[random.randint(0,20) for i in range(10)]
print(list)
print(sort(list))
