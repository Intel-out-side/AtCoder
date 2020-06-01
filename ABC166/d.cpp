#include <bits/stdc++.h>
using namespace std;
using ll = long long;

vector<pair<ll, ll>> factorize(ll n) {
  vector<pair<ll, ll>> res;
  //√n までを見れば良いので終了条件がi^2<=nになる
  for (ll i = 2; i * i <= n; i++) {
    if (n%i != 0) continue;
    res.emplace_back(i, 0);//res.push_back(make_pair(i, 0));と同等
    while (n % i == 0) {
      n /= i;
      res.back().second++;
    }
  }
  //最初のn自体が
  if (n != 1) res.emplace_back(n, 1);
  return res;
}

int main() {
  ll X;
  cin >> X;

  ll A = 0;

  while (true) {
    ll B_5 = A * A * A * A * A - X;

    vector<pair<ll, ll>> fact = factorize(B_5);

    if (fact[0].second == 5) {
      cout << A << " " << fact[0].first << endl;
      break;
    }

    A++;

  }

  return 0;
}
