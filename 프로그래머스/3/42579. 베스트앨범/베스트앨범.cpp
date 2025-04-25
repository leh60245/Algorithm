#include <bits/stdc++.h>

using namespace std;
using vi = vector<int>;
using pii = pair<int, int>;


vector<int> solution(vector<string> genres, vector<int> plays) {
    vector<int> answer;
    unordered_map<string, int> genre_num;
    unordered_map<string, vector<pii>> song_in_genre;
    
    int N = genres.size();
    for (int i = 0 ; i < N ; i++){
        string genre = genres[i];
        genre_num[genre] += plays[i];
        song_in_genre[genre].push_back({plays[i], i});
    }
    vector<pair<string, int>> sorted_genre_num(genre_num.begin(), genre_num.end());
    sort(sorted_genre_num.begin(), sorted_genre_num.end(), [](const auto& a, const auto& b){
       return a.second > b.second; 
    });
    
    // for (auto& p : sorted_genre_num) cout << p.second << ' ';
    for (auto& [name, n] : sorted_genre_num){
        auto& songs = song_in_genre[name];
        sort(songs.begin(), songs.end(), [](const auto& a, const auto& b){
            if (a.first != b.first) return a.first > b.first;
            return a.second < b.second;
            
        });
        for (int i=0 ; i < 2 && i < songs.size(); i++ ) answer.push_back(songs[i].second);
    }
    
    
    return answer;
}