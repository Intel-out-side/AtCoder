#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using P = pair<int, int>;

const ll INF = (ll)(1e18)+1;

//よくわかんなかったので要復習と思われる
int main() {
  //二分探索で解く
  int n; ll k;
  cin >> n >> k;
  vector<ll> A(n);
  for (ll i = 0; i < n; i++) cin >> A[i];
  sort(A.begin(), A.end());
  ll l = -INF, r = INF;
  while (l + 1 < r) {
    ll x = (l+r)/2;
    bool ok = [&]{
      ll tot = 0;
      for (ll i = 0; i < n; i++) {
        if (A[i] < 0) {
          int l = -1, r = n;
          while (l + 1 < r) {
            int c = (l+r)/2;
            if (A[c] * A[i] < x) r = c; else l = c;
          }
          tot += n - r;
        }
        else {
          int l = -1, r = n;
          while (l+1 < r) {
            int c = (l+r)/2;
            if (A[c] * A[i] > x) l = c; else r = c;
          }
          tot += r;
        }
        if (A[i] * A[i] < x) tot--;
      }
      tot /= 2;
      return tot < k;
    }();
    if (ok) l = x; else r = x;
  }
  cout << l << endl;
  return 0;
}
