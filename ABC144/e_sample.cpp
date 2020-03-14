#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
  ll n, k;
  cin >> n >> k;

  vector<ll> A(n), F(n);
  for (ll i = 0; i < n; i++) cin >> A[i];
  for (ll i = 0; i < n; i++) cin >> F[i];

  sort(A.begin(), A.end()); //ascending order
  sort(F.begin(), F.end());
  reverse(F.begin(), F.end()); //descending order

  //決め打ちで二分探索する
  ll l = -1; //leftは絶対にfalseになる値にする
  ll r = (ll)1e12+1;

  while (l+1 < r) {
    ll mid = (l + r) / 2;
    bool ok = [&]{
      ll sum = 0;
      for (ll i = 0; i < n; i++) {
        sum += max(0ll, A[i]-mid/F[i]);
      }
      return sum <= k;
    }();

    if (ok) r = mid;
    else l = mid;
  }

  cout << r << endl;
  return 0;
}
