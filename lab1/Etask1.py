from collections import deque

def main():
    a = deque(map(int, input().split()))
    b = deque(map(int, input().split()))

    cnt = 0
    while cnt <= 1000000 and a and b:
        cnt += 1
        x, y = a.popleft(), b.popleft()

        
        if (x == 0 and y == 9) or (x > y and not (x == 9 and y == 0)):
            a.append(x)
            a.append(y)
        else:
            b.append(x)
            b.append(y)

    if cnt > 1000000:
        print("blin nichiya")
    elif not a:
        print("Nursik", cnt)
    else:
        print("Boris", cnt)

if __name__ == "__main__":
    main()
