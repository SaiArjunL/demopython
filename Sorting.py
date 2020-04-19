p = 0
def fun(l):
    for i in range(len(l)-1,0,-1):
        for j in range(i):
            if l[j] > l[j+1]:
                p = l[j]
                l[j] = l[j+1]
                l[j+1] = p
    return l


l = [5,1,6,8,12,16,34,32,9,13,14,71,39,7]

print(fun(l))
