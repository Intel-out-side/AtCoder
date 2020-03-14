#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using P = pair<ll, ll>;

template <typename T> T gcd(T a, T b) {
  if (a % b == 0) {
    return b;
  }
  else {
    return (gcd(b, a%b));
  }
}

struct Sieve {
  int n;
  vector<ll> f, primes;
  Sieve(ll n = 1): n(n), f(n + 1) {
    f[0] = f[1] = -1;
    for (ll i = 2; i <= n; i++) {
      if (f[i]) continue; //印がなければ素数扱い
      primes.push_back(i);
      for (ll j = i; j <= n; j += i) {
        f[j] = i; //iの倍数のところに印をつけていく
      }
    }
  }

  bool isPrime(ll x) { return f[x] == x; }

  //ｘを素因数分解する関数
  // return -> 素因数
  vector<ll> factorList(ll x) {
    vector<ll> res;
    while (x != 1) {
      res.push_back(f[x]);
      x /= f[x];
    }
    return res; //大きい順で素因数がvectorに格納されて出てくる
  }

  //各素因数が何乗されているかをpair typeで返す
  vector<P> factorPower(ll x) {
    vector<ll> factors = factorList(x);
    if (factors.size() == 0) return {};
    vector<P> res(1, P(factors[0], 0));
    for (ll p : factors) {
      if (res.back().first == p) {
        res.back().second ++;
      }
      else {
        res.emplace_back(p, 1);
      }
    }
      return res;
    }
  };

int main() {
  ll A, B;
  cin >> A >> B;

  ll g = gcd(A, B);

  Sieve s = Sieve(g);

  vector<P> f = s.factorPower(g);

  ll ans = f.size() + 1;

  cout << ans << endl;
  return 0;
}
