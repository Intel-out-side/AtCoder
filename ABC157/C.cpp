#include <bits/stdc++.h>
using namespace std;

int main() {
  int N, M;
  cin >> N >> M;

  vector<pair<int, int>> s_c(M);
  for (int i = 0; i < M; i++) {
    int s, c;
    cin >> s >> c;
    s_c[i] = make_pair(s, c);
  }

  int min = 10000;
  string str_result = to_string(min);
  str_result[0] = '0';

  for (int i = 0; i < M; i++) {
    str_result[s_c[i].first - 1] = (char)(s_c[i].second + 0x30);
  }

  if (str_result[0] == '0') {
    cout << -1 << endl;
    return 0;
  }

  int right_most = str_result.length() - 1;
  while (true) {
    if (str_result[right_most] == '0') right_most--;
    else break;
  }

  str_result = str_result.substr(0, str_result.length() - right_most);
  min = (int) pow(10, N-1);

  int num = atoi(str_result.c_str());
  cout << str_result << endl;

  return 0;
}
