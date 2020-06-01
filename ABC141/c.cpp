#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
  ll N, K, Q;
  cin >> N >> K >> Q;
  vector<ll> p(N, 0);
  for (ll i = 0; i < Q; i++) {
    ll who;
    cin >> who;
    p[who - 1]++;
  }

  for (ll i = 0; i < N; i++) {
    if (K - (Q - p[i]) > 0) cout << "Yes" << endl;
    else cout << "No" << endl;
  }

  return 0;
}
