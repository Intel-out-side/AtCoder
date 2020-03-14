#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
  ll N;
  cin >> N;
  vector<ll> tk(N);
  for (ll i = 0; i < N; i++) cin >> tk[i];

  ll s = 0;
  for (ll i = 0; i < N; i++) {
    for (ll j = i + 1; j < N; j++) {
      s += tk[i] * tk[j];
    }
  }
  cout << s << endl;
  return 0;
}
