/*
DONT FORGET
#include <vector>
#include
*/
typedef long long ll;

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

ll GCD(vector<ll> x) {
}
