//全探索してしまえばいいという問題

#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
  ll X;
  cin >> X;

  for (ll i = -1000; i <= 1000; i++) {
    for (ll j = -1000; j <= 1000; j++) {
      ll ans = i * i * i * i * i - j * j * j * j * j;
      if (ans == X) {
        cout << i << " " << j << endl;
        return 0;
      }
    }
  }
  return 0;
}
