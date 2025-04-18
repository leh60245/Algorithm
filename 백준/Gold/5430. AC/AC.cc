#include <bits/stdc++.h>
using namespace std;

/*
 * AC: 정수 배열에 연산을 하기 위해 만든 언어
 * [두 함수 R/D]
 * R: 배열에 있는 수의 순서를 뒤집기
 * D: 첫 번째 수를 버리기. 배열이 비어 있는데 D를 사용하면 에러
 *
 * 함수는 조합해서 한 번에 사용할 수 있다.
 * RDD는 배열을 뒤집은 다음 처음 두 수를 버리는 함수
 *
 * [목표] 배열의 초기값과 수행할 함수 주어짐
 * 최종 결과 구하기
 * 단, ERROR 가 발생하는 경우에는 "error" 출력
 */

void parse(string& tmp, deque<int>& d)
{
    int cur = 0;
    for (int i=1; i+1<tmp.size(); i++)
    {
        if (tmp[i] == ',')
        {
            d.push_back(cur);
            cur = 0;
        } else
        {
            cur = 10 * cur + (tmp[i] - '0');
        }
    }
    if (cur!=0)
        d.push_back(cur);
}

void print_result(deque<int>& q)
{
    cout << '[';
    for (int i=0; i< q.size(); i++)
    {
        cout << q[i];
        if (i+1 != q.size())
            cout << ',';
    }
    cout << ']' << '\n';
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    int T;
    cin >> T;
    while (T--)
    {
        int n, rev = 0;
        deque<int> q;
        string query, tmp;
        bool is_wrong = false;
        cin >> query;
        cin >> n;
        cin >> tmp;


        parse(tmp, q);
        for (char c: query)
        {
            if (c=='R') rev = 1 - rev;
            else
            {
                if (q.empty())
                {
                    is_wrong = true;
                    break;
                }
                if (!rev) q.pop_front();
                else q.pop_back();
            }
        }
        if (is_wrong) cout << "error\n";
        else
        {
            if (rev) reverse(q.begin(), q.end());
            print_result(q);
        }

    }

}
