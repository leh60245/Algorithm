#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    set<string> words;

    while (N--) {
        string word;
        cin >> word;
        words.insert(word);
    }

    vector<string> sorted(words.begin(), words.end());
    sort(sorted.begin(), sorted.end(), [](const string& a, const string& b) {
        if (a.size() == b.size()) return a < b;
        return a.size() < b.size();
    });

    for (const auto& word : sorted)
        cout << word << '\n';
}
