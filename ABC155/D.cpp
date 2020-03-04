#include <bits/stdc++.h>
using namespace std;
using ll = long long;

bool sort2(const ll &a, const ll &b) {
  return a < b;
}

int main() {
  ll N, K;
  cin >> N >> K;
  vector<ll> A(N);
  for (ll i = 0; i < N; i++) cin >> A[i];

  vector<long long> p(N*(N-1)/2);

  for (ll i = 0; i < N; i++) {
    for (ll j = i; j < N; j++) {
      p.push_back(A[i] * A[j]);
    }
  }

  sort(p.begin(), p.end(), sort2);

  cout << p[K] << endl;
}
