#include <bits/stdc++.h>
using namespace std;

int main() {
  int n;
  cin >> n;
  string s;
  cin >> s;

  for (int i = 0; i < s.length(); i++) {
    s[i] += n;
    if (s[i] > 90) s[i] -= 26;
  }

  cout << s << endl;
  return 0;
}
