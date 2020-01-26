#include <bits/stdc++.h>
#define rep(i, n) for(unsigned long long i = 0; i < n; i++)
#define MAX 2 * 1e9
using namespace std;
using ll = unsigned long long;

ll gcd(ll a, ll b) {
  if (a < b) {
    ll tmp = a;
    a = b;
    b = tmp;
  }

  ll r = a % b;
  while ( r != 0 ) {
    a = b;
    b = r;
    r = a % b;
  }

  return b;
}

ll lcm(ll a, ll b) {
  ll result = a * b / gcd(a, b);
  if (result > MAX) return 0;
  return result;
}

ll LCM(vector<ll> x) {
  ll ans = lcm(x[0], x[1]);
  for (ll i = 0; i < x.size(); i++) {
    ans = lcm(ans, x[i]);
  }
  return ans;
}

ll reduce(ll x) {
  ll sum = 0;
  while (x % 2 == 0) {
    sum++;
    x /= 2;
  }
  return sum;
}

int main() {
  ll N, M;
  cin >> N >> M;
  M *= 2;
  vector<ll> a(N), reduced_a(N);
  rep(i, N) cin >> a[i];

  rep(i, N) reduced_a[i] = reduce(a[i]);
  bool divisible_same = true;
  rep(i, N - 1) {
    if (reduced_a[i] != reduced_a[i+1]) divisible_same = false;
  }

  if (!divisible_same) {
    cout << 0 << endl;
    return 0;
  }
  else {
    ll lcm = LCM(a), lcm_ = lcm;
    if (lcm == 0) {
      cout << 0 << endl;
      return 0;
    }
    if (lcm > M) {
      cout << 0 << endl;
      return 0;
    }
    else {
      ll sum = 0, count = 1;
      while (lcm_ <= M) {
        sum++;
        lcm_ = lcm * (2*count + 1);
        count++;
      }

      cout << sum << endl;
      return 0;
    }
  }
}
