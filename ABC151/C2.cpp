#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < n; i++)
using namespace std;
using ll = long long;

int main (){
  int n, m;
  cin >> n >> m;
  map<int, vector<string>> result;
  vector<int> p(m);
  vector<string> s(m);

  rep(i, m) {
    cin >> p[i] >> s[i];
    if (result[p[i]].empty()) { result[p[i]] = vector<string>();}
    result[p[i]].push_back(s[i]);
  }

  int ACs = 0, penalties = 0;
  for (pair<int, vector<string>> p : result) {
    int key = p.first;
    vector<string> value = p.second;
    bool ACed = false;
    int i = 0;
    int WAs = 0;
    while (!ACed) {
      if (p.second[i] == "WA") WAs++;
      if (p.second[i] == "AC") ACed = true;
      i ++;
      if (p.second.size() == i) break;
    }

    if (ACed) {
      ACs++;
      penalties += WAs;
    }
  }

  cout << ACs << " " << penalties << endl;
  return 0;

}
