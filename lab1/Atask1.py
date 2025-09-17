from collections import deque

t = int(input())
for _ in range(t):
    x = int(input())
    a = [-1] * x
    dq = deque(range(x))  

    for cur in range(1, x + 1):
        cnt = (cur + 1 - 1) % len(dq)   
        dq.rotate(-cnt)                 
        pos = dq.popleft()              
        a[pos] = cur                    

    print(*a)
