#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
  ll N, K;
  cin >> N >> K;

  ll ans = 0;
  for (ll i = 0; i < N; i++) {
    ll tmp;
    cin >> tmp;
    if (tmp >= K) ans++;
  }

  cout << ans << endl;
  return 0;
}
