num= int(input())
for i in range(3,num):
    a = num%i
    if (a ==0):
        print(num,'是合数')
        break
    if (i ==num-1):
        print(num,'是质数')
