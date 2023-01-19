n = int(input())
answer = 0

for _ in range(n):
    str = input().rstrip()
    st = []
    for s in str:
        if not st:
            st.append(s)
            continue
        if st[-1] == s:
            st.pop()
        else:
            st.append(s)

    if not st:
        answer += 1

print(answer)