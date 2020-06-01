#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
  string S, T;
  cin >> S >> T;

  if (T.substr(0, T.length()-1) == S) cout << "Yes" << endl;
  else cout << "No" << endl;
  return 0;
}
