#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
  string S;
  cin >> S;
  ll K;
  cin >> K;

  if (S.length() == 1) {
    cout << K/2 << endl;
    return 0;
  }

  ll count = 0;
  for (int i = 0; i < S.length()-1; i++) {
    if (S[i] == S[i+1]) {
      S[i+1] = '*';
      count ++;
    }
  }

  if (S[0] == S[S.length()-1]) {
    count++;
    S[S.length()-1] = '*';
    cout << S << endl;

    ll res;
    if (K == 1) {
      res = count * K;
    }
    else {
      res = count * K - 1;
    }
    cout << res << endl;
    return 0;
  }
  else {
    cout << S << endl;
    ll res = count * K;

    cout << res << endl;
    return 0;
  }
}
