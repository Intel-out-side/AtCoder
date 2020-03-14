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
  ll left = -1; //leftは絶対にfalseになる値にする
  ll right = (ll)1e12+1;

  while (left + 1 < right) {
    ll mid = (left + right)/2;
    double reduce_sum = 0;
    for (ll i = 0; i < n; i++) {
      reduce_sum += max(0LL, A[i] - mid/F[i]);
    }
    if (reduce_sum <= k) right = mid;
    else left = mid;
  }

  cout << right << endl;
  return 0;
}
