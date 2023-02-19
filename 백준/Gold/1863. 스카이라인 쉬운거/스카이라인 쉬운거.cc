#include<iostream>
#include<stack>
using namespace std;

int main(void)
{
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    int n,x,y;
    int total=0;
    stack<int> st;

    st.push(0);
    cin>>n;

    while(n--)
    {
        cin>>x>>y;

        if(st.top()<y) 
        {
            st.push(y);
        }

        if(st.top()>y)
        {
            while(st.top()>y)
            {
                st.pop();
                if(st.top()<y) st.push(y);
                total++;
            }
           
        }
    }

    while(st.top()!=0)
    {
        st.pop();
        total++; //0으로 끝나지 않아서 스택에 남아있을 경우 
    }

    cout<<total;
    return 0;
}
