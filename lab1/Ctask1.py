def process(st):
    ans = []
    for ch in st:
        if ch == "#":
            if ans:  # чтобы не было ошибки, если список пуст
                ans.pop()
        else:
            ans.append(ch)
    return "".join(ans)

# читаем две строки из одной строки ввода
s, t = input().split()

ans1 = process(s)
ans2 = process(t)

if ans1 == ans2:
    print("Yes")
else:
    print("No")
