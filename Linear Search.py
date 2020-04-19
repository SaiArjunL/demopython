p = 0


def search(l, n):
    f = 0
    m = len(l) - 1
    while f <= m:
        mid = (f + m) // 2
        if l[mid] == n:
            globals()['p'] = mid
            return True
        else:
            if l[mid] < n:
                f = mid + 1
            else:
                m = mid - 1
    return False


def sort(l):
    for i in range(len(l) - 1, 0, -1):
        for j in range(i):
            if l[j] > l[j + 1]:
                q = l[j]
                l[j] = l[j + 1]
                l[j + 1] = q

    return l


l = [5, 1, 6, 8, 12, 16, 34, 32, 9, 13, 14, 71, 39, 7]
n = 32

print(sort(l))

if search(l, n):
    print("Found at ", p + 1)
else:
    print("Not Found")
