#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N, M;
vector<int> arr;
int answer[10];
bool visited[10];

void backtraking(int depth) {
	if (depth == M) {
		for (int i = 0; i < M; i++) cout << answer[i] << ' ';
		cout << '\n';
		return;
	}
	for (int i = 0; i < N; i++) {
		if (!visited[i]) {
			visited[i] = true;
			answer[depth] = arr[i];
			backtraking(depth + 1);
			visited[i] = false;
		}
	}
	return;
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	
	cin >> N >> M;
	for (int i = 0; i < N; i++) {
		int x;
		cin >> x;
		arr.push_back(x);
	}
	sort(arr.begin(), arr.end());
	
	backtraking(0);

	return 0;
}