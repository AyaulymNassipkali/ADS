n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    ok = False
    for j in range(i - 1, -1, -1):  # идём влево от i-1 к 0
        if a[j] <= a[i]:
            print(a[j], end=" ")
            ok = True
            break
    if not ok:
        print(-1, end=" ")
