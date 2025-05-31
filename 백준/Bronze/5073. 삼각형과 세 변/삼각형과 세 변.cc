#include <bits/stdc++.h>
using namespace std;
using vi = vector<int>;
using vvi = vector<vi>;


int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int a, b, c;
    while (true)
    {
        cin >> a >> b >> c;
        if (a == 0 && b == 0 && c == 0) break;
        vi arr = {a, b, c};
        sort(arr.begin(), arr.end());
        // 삼각형이 아닌 경우
        if (arr[2] >= arr[0] + arr[1]) cout << "Invalid\n";
        else if (arr[0] == arr[1] && arr[1] == arr[2]) cout << "Equilateral\n";
        else if (arr[0] == arr[1] || arr[1] == arr[2]) cout << "Isosceles\n";
        else cout << "Scalene\n";
    }
    return 0;
}
