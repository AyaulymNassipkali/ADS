def main():
    s = input().strip()

    if not s:   
        print("NO")
        return

    st = []   
    st.append(s[0])

    for i in range(1, len(s)):
        current = s[i]
        if st and st[-1] == current:   # если вершина стека совпадает с текущим символом
            st.pop()
        else:
            st.append(current)

    if not st:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
