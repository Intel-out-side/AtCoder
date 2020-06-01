#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
  ll N;
  cin >> N;

  vector<ll> A(N + 1);
  for (int i = 2; i <= N; i++) cin >> A[i];

  map<ll, ll> m;

  for (int i = 2; i <= N; i++) {
    m[A[i]] ++;
  }

  for (ll i = 1; i <= N; i++) {
    cout << m[i] << endl;
  }

  return 0;
}
