#include <bits/stdc++.h>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    string answer = "";
    unordered_map<string, int> par;
    for (string name : participant) par[name]++;
    for (string name : completion) par[name]--;
    for (auto& p : par){
        if (p.second >= 1) return p.first;
    }
    return answer;
}