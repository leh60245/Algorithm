#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false); // 입출력 속도 향상
    cin.tie(nullptr);            // cin과 cout을 묶지 않음

    int N;
    cin >> N;
    vector<int> cards(N);
    for (int i = 0; i < N; ++i)
        cin >> cards[i];

    sort(cards.begin(), cards.end()); // 이분 탐색을 위한 정렬

    int M;
    cin >> M;
    while (M--) {
        int num;
        cin >> num;
        // binary_search는 STL에서 제공하는 이분 탐색 함수
        cout << binary_search(cards.begin(), cards.end(), num) << ' ';
    }
    cout << '\n';
    return 0;
}
