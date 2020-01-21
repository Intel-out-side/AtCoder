#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const ll MAX = 200000 + 1;

int main() {
  ll N;
  ll ans = MAX;
  ll index = 1;
  ll destroy = 0;
  cin >> N;
  vector<ll> a(N);

  for (int i = 0; i < N; i++) cin >> a[i];

  for (ll i = 1; i <= N; i++) {
    if (index != a[i - 1]) {
      destroy++;
    }
    else if (index == a[i - 1]){
      index++;
    }
  }

  if (destroy == N) {
    cout << -1 << endl;
  }
  else {
    cout << destroy << endl;
  }

  return 0;
}
