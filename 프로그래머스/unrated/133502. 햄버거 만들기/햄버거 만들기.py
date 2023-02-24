def solution(ingredient):
    st = []
    answer = 0
    
    flag = False
    for i in ingredient:
        if i == 1 and len(st) >= 3 and st[-1] == 3 and st[-2] == 2 and st[-3] == 1:
            for _ in range(3):
                st.pop()
            answer += 1
            continue
        st.append(i)
    
    return answer