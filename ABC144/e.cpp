#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
  ll n, k;
  cin >> n >> k;

  vector<ll> A(n), F(n);
  for (ll i = 0; i < n; i++) {
    cin >> A[i];
  }
  for (ll i = 0; i < n; i++) {
    cin >> F[i];
  }

  sort(A.begin(), A.end());
  sort(F.begin(), F.end());
  reverse(F.begin(), F.end());

  vector<ll> accum_sum(n);
  accum_sum[0] = A[0];
  for (ll i = 1; i < n; i++) {
    accum_sum[i] = accum_sum[i-1] + A[i];
  }

  ll idx = 0;
  while (idx < n) {
    accum_sum[idx] = 0;
    if (accum_sum[idx] >= k) {
      A[idx] -= accum_sum[idx] - k;
      break;
    }
    idx++;

  }

  ll maxv = 0;
  for (ll i = 0; i < n; i++) {
    maxv = max(maxv, A[i]*F[i]);
  }

  cout << maxv << endl;
  return 0;
}
