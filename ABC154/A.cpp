#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < n; i++)
using namespace std;

int main() {
  int a, b;
  string s, t, u;

  cin >> s >> t;
  cin >> a >> b;

  cin >> u;

  if (s == u) {
    a--;
  }
  else if (t == u) {
    b--;
  }

  cout << a << " " << b << endl;
  return 0;
}
