#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
  ll N, M;
  cin >> N >> M;
  vector<ll> H(N);
  vector<bool> is_good_peak(N, true);
  for (ll i = 0; i < N; i++) cin >> H[i];

  for (ll i = 0; i < M; i++) {
    ll A, B;
    cin >> A >> B;
    A--; B--;

    if (H[A] <= H[B]) is_good_peak[A] = false;
    if (H[B] <= H[A]) is_good_peak[B] = false;
  }

  ll ans = 0;
  for (bool item : is_good_peak) {
    if (item) ans++;
  }

  cout << ans << endl;
  return 0;
}
