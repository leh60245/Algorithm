#include <bits/stdc++.h>
using namespace std;
using vi = vector<int>;
using vvi = vector<vi>;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

   while (true)
   {
       int a, b, c; cin >> a >> b >> c;
       if (a==0) break;
       vi arr = {a, b, c};
       sort(arr.begin(), arr.end());
       if (arr[0] * arr[0] + arr[1] * arr[1] == arr[2] * arr[2])
           cout << "right\n";
       else
           cout << "wrong\n";
   }
}
