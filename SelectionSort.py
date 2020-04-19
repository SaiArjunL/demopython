def sort(l):
    for i in range(len(l) - 1):
        minp = i
        for j in range(i, len(l)):
            if l[j] < l[minp]:
                minp = j

        p = l[i]
        l[i] = l[minp]
        l[minp] = p


l = [5, 1, 6, 8, 12, 16, 34, 32, 9, 13, 14, 71, 39, 7]

sort(l)

print(l)
