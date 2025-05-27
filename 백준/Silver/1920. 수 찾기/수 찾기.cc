#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false); // 입출력 속도 향상
    cin.tie(nullptr); // cin과 cout을 묶지 않음

    int N;
    cin >> N;
    vector<int> A(N);

    for (int i = 0; i < N; i++) {
        cin >> A[i]; // 배열 입력
    }

    sort(A.begin(), A.end()); // 이분 탐색을 위해 정렬

    int M;
    cin >> M;

    while (M--) {
        int x;
        cin >> x;

        // binary_search 함수는 STL에서 제공하는 이분 탐색 함수야.
        if (binary_search(A.begin(), A.end(), x)) {
            cout << 1 << '\n'; // 존재함
        } else {
            cout << 0 << '\n'; // 존재하지 않음
        }
    }

    return 0;
}
