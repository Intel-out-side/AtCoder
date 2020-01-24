#include <bits/stdc++.h>
#include <algorithm>
#define rep(i, n) for(long long i = 0; i < n; i++)
using namespace std;
using ll = long long;

ll gcd(ll a, ll b) {
  if (a % b == 0) {
    return b;
  }
  else {
    return (gcd(b, a%b));
  }
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

ll reduce(ll x) {
  while (x % 2 == 0) {
    x /= 2;
  }
  return x;
}

int main() {
  ll N, M;
  cin >> N >> M;
  M *= 2;
  vector<ll> a(N);
  rep(i, N) cin >> a[i];

  //rep(i, N) a[i] = reduce(a[i]);

  ll lcm = LCM(a), lcm_ = lcm;
  ll sum = 0, count = 1;
  while (lcm_ <= M) {
    sum++;
    lcm_ = lcm * (2*count + 1);
    count++;
  }

  cout << sum << endl;
  return 0;
}
