#include <bits/stdc++.h>
using namespace std;

int t, d, n, s, p;
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        cin >> d >> n >> s >> p;
        // 병렬버전 프로그램 개발, 개발하는 데 걸리는 시간
        // 병렬버전과 직렬버전의 실행 시간 측정
        // 작업령 최소화 목적
        // 작업량 = '병렬 버전 개발하는 시간' + '그 프로그램이 실행될 때까지 기다리는 시간'
        // d = 병렬버전 개발하는데 걸리는 시간
        // n = 다음해 동안 이 프로그램이 실행되는 횟수
        // s = 직렬버전 실행 시간
        // p = 병렬버전 실행시간
        if (d + n*p < n*s) cout << "parallelize\n";
        else if (d + n*p > n*s) cout << "do not parallelize\n";
        else cout << "does not matter\n";
    }
    return 0;
}
