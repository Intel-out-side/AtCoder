#include <bits/stdc++.h>
using namespace std;
using ll = long long;

ll gcd(ll x, ll y) {
  return y ? gcd(y, x%y) : x;
}

vector<pair<ll, int>> factorize(ll n) {
  vector<pair<ll, int>> res;
  for (ll i = 2; i * i <= n; i++) {
    if (n%i) continue; //割り切れないならcontinue
    res.emplace_back(i, 0);
    while (n%i == 0) {
      n /= i;
      res.back().second++;
    }
  }
  if (n != 1) res.emplace_back(n, 1);
  return res;
}

//約数は最大公約数の約数になる
int main() {
  ll A, B;
  cin >> A >> B;
  ll g = gcd(A, B);
  ll ans = factorize(g).size() + 1;
  cout << ans << endl;
  return 0;
}
