def Square_root_1():
    c=2
    g=0
    for j in range(0,c+1):
        if(j*j>c and g == 0):
            g = j-1
    while(abs(g*g - c) > 0.001):
        g += 0.001
    print(g)
Square_root_1()
