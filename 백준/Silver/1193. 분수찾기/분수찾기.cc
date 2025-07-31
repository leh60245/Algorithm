// main.cpp
#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int X;
    cin >> X;

    int line = 1; // 현재 몇 번째 대각선인지
    int sum = 0;  // 현재까지 몇 개의 항이 있는지 누적합

    // 몇 번째 대각선인지 찾기
    while (sum + line < X) {
        sum += line;
        line++;
    }

    // line번째 대각선에서 몇 번째인지
    int offset = X - sum;

    int numerator, denominator;
    if (line % 2 == 1) {
        // 홀수 대각선: 위에서 아래로 (예: 3/1, 2/2, 1/3)
        numerator = line - offset + 1;
        denominator = offset;
    } else {
        // 짝수 대각선: 아래에서 위로 (예: 1/4, 2/3, 3/2, 4/1)
        numerator = offset;
        denominator = line - offset + 1;
    }

    cout << numerator << '/' << denominator << '\n';
    return 0;
}
