t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    x = [0]*m
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    for i in range(m):
        x[i] = -1
    for i in range(0, n):
        if x[a[i]] == -1:
            x[a[i]] = 0
            x[a[i]] += b[i]
    min = 10000
    for i in range(m):
        if x[i] != -1:
            if x[i] < min:
                min = x[i]
    print(min)
