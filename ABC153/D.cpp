#include <bits/stdc++.h>
#define rep(i, n) for(long long i = 0; i < n; i++)
using namespace std;
using ll = long long;
using P = pair<int, int>;

ll ap2(ll x, ll n) {
  if (x == 1) return n;
  else ap2(x/2, n+1);
}

ll pow(ll a, ll b) {
  ll res = 1;
  for (ll i = 1; i <= b; i++){
    res *= a;
  }
  return res;
}

int main() {
  ll H;
  ll sum = 0, res = 0;
  cin >> H;

  res = ap2(H, 0);

  for (ll i = 0; i <= res; i++) {
    sum += pow(2, i);
  }
  cout << sum << endl;

  return 0;
}
