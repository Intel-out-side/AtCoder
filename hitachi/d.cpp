#include <bits/stdc++.h>
using namespace std;
#define MAX 10001001
using ll = long long;
using p = pair<ll, ll>;

int main() {
  ll N, T;
  cin >> N >> T;

  vector<p> a_b(N);
  for (ll i = 0; i < N; i++) {
    ll a, b;
    cin >> a >> b;
    a_b[i] = make_pair(a, b);
  }

  vector<vector<ll>> M(N+1, vector<ll>(T+1, 0));

  for (ll i = 1; i <= N; i++) {
    for (ll t = 0; t <= T; t++) {
      if (t + (a_b[i].first * t + a_b[i].second) > T) continue;

      if (M[i][t - a[i].first * t - a_b[i].second] > M[i][t]) M[i][t] = M[i][t - a[i].first * t - a_b[i].second] + 1;
    }
  }

}
