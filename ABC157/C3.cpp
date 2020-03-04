#include <bits/stdc++.h>
using namespace std;

int main() {
  int N, M;
  cin >> N >> M;

  vector<pair<int, int>> s_c(M);
  map<int, int> m;
  for (int i = 0; i < M; i++) {
    int s, c;
    cin >> s >> c;
    s_c[i] = make_pair(s, c);
    m[s-1] = c;
  }

  int num = 0;
  map<int, int> iterator :: it;
  for (it = m.begin(); it < m.end(); it++) {
    num += (int) pow(10, it->first) * it->second;
  }

  cout << num << endl;
  return 0;
}
