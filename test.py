def solve():
    n, k = [int(_) for _ in input().split()]
    a = [int(_) for _ in input().split()]
    l = 0
    cl = 0
    for i in range(0, n, k):
        for j in range(k):
            cl = i + j
            for jj in range(i + j + k, n, k):
                if a[jj] != 0 and (a[cl] == 0 or a[jj] < a[cl]):
                    cl = jj
            if a[cl] < l:
                return "no"
            l = a[cl]
            a[cl] = a[i+j]
            a[i+j] = 0
    return "yes"

for _ in range(int(input())):
    print(solve())