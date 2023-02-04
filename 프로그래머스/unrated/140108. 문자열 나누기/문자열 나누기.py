def solution(s):
    answer = 0
    st = []
    
    for c in s:
        if not st:
            answer += 1
            st.append(c)
            continue
        if st[-1] == c:
            st.append(c)
        elif st:
            st.pop()
    
    return answer