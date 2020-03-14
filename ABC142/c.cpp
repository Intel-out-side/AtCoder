#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
  ll N;
  cin >> N;
  vector<pair<ll, ll>> A(N);

  for (ll i = 0; i < N; i++) {
    ll tmp;
    cin >> tmp;
    A[i] = make_pair(tmp, i);
  }

  sort(A.begin(), A.end());

  for (ll i = 0; i < N; i++) {
    if (i > 0) cout << " ";
    cout << A[i].second + 1;
  }
  cout << endl;
  return 0;
}
