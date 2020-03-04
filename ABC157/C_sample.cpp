#include <bits/stdc++.h>
using namespace std;

/*
  1. 問題文をよく読みましょう
  2. (s, c) = (1, 2), (1, 3)だったときに、ひと桁目が2かつ3になるようなやつを考えるので必ずfalseになる
*/
int main() {
  int n, m;
  cin >> n >> m;

  vector<pair<int, int>> s_c(m);
  map<int, int> mp;
  for (int i = 0; i < m; i++) {
    int s, c;
    cin >> s >> c;
    s_c[i] = make_pair(s, c);
    mp[s] = c;
  }

  int num = 0;
  while (num < 1000) {
    string str_num = to_string(num);
    if (str_num.length() != n) {
      num++;
      continue;
    }

    bool okay = true;
    for (auto p : mp) {
      int digit = str_num[p.first - 1] - 0x30;
      if (digit != p.second) okay = false;
    }
    /*
    for (int i = 0; i < m; i++) {
      int digit = str_num[s_c[i].first - 1] - 0x30;
      if (digit != s_c[i].second) okay = false;
    }
    */

    if (okay) {
      cout << num << endl;
      return 0;
    }

    num ++;
  }

  cout << -1 << endl;
  return 0;
}
