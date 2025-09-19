#include <iostream>

using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int N;
	cin >> N;
	int answer = 0;
	for (int i = 0; i < N; i++) {
		int x; cin >> x;
		answer += x;
	}
	if ((N / 2) >= answer) cout << "Junhee is not cute!";
	else cout << "Junhee is cute!";

	return 0;
}