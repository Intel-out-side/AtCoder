#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
  ll N;
  cin >> N;
  vector<ll> A(N);
  map<ll, ll> M;
  map<ll, pair<ll,ll>> ansMap;

  for (ll i = 0; i < N; i++) {
    ll tmp;
    cin >> tmp;
    A[i] = tmp;
    M[tmp]++;
  }

  // a 多い方
  for (auto item : M) {
    ll a = max((ll)0, item.second*(item.second-1)/2);
    ll b = max((ll)0, (item.second-1)*(item.second-2)/2);
    ansMap[item.first] = make_pair(a, b);
  }

  ll SUM = 0;
  for (auto item : ansMap) {
    SUM += item.second.first;
  }

  for (ll i = 0; i < N; i++) {
    cout << SUM - M[A[i]]+1 << endl;
  }

/*
  for (ll i = 0; i < N; i++) {
    ll ans = 0;
    for (auto item : M) {
      if (item.first == A[i]) ans += max((ll)0, (item.second-1)*(item.second-2)/2);
      else ans += max((ll)0, item.second*(item.second-1)/2);
    }
    cout << ans << endl;
  }
  */
  return 0;
}
