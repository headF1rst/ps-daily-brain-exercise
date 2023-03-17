ss = list(input())
st = []
answer = ''

for s in ss:
    if s.isalpha():
        answer += s
        continue
    if s == '(':
        st.append(s)
    elif s == '*' or s == '/':
        while st and (st[-1] == '*' or st[-1] == '/'):
            answer += st.pop()
        st.append(s)
    elif s == '+' or s == '-':
        while st and st[-1] != '(':
            answer += st.pop()
        st.append(s)
    elif s == ')':
        while st and st[-1] != '(':
            answer += st.pop()
        st.pop()

while st:
    answer += st.pop()
print(answer)