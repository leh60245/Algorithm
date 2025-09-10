#include <iostream>
#include <vector>
using namespace std;

int N, M;
int answer[10];
//int visited[10];

void backtraking(int count, int start) {
	if (count == M) {
		for (int i = 0; i < M; i++) cout << answer[i] << ' ';
		cout << '\n';
		return;
	}
	for (int i = start; i <= N; i++) {
		answer[count] = i;
		backtraking(count + 1, start);
	}
	return;
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	
	cin >> N >> M;
	backtraking(0, 1);

	return 0;
}