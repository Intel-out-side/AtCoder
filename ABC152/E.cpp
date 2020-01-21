#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long ll;

ll gcd(ll a, ll b) {
  if (a < b) {
    ll tmp = a;
    a = b;
    b = tmp;
  }
  ll r = a % b;
  while (r != 0) {
    a = b;
    b = r;
    r = a % b;
  }

  return b;
}

ll lcm(ll a, ll b) {
  return a * b / gcd(a, b);
}

ll LCM(vector<ll> x) {
  ll ans = lcm(x[0], x[1]);
  for (ll i = 0; i < x.size(); i++) {
    ans = lcm(ans, x[i]);
  }
  return ans;
}

int main() {
  int N;
  vector<ll> A(N);
  ll sum = 0;
  ll const devider = 10e9 + 7;
  for (ll i = 0; i < N; i++) cin >> A[i];
  ll const x = LCM(A);
  for (ll i = 0; i < N; i++) sum += x / A[i];

  cout << sum % devider << endl;
  return 0;
}
