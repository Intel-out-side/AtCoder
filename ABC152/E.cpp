//#include <bits/stdc++.h>
#include <iostream>
#include <vector>
#include <map>
#define rep(i, n) for (int i = 0; i < n; i++)
using namespace std;
typedef long long ll;
typedef pair<int, int> P;

// auto mod int
// https://youtu.be/L8grWxBlIZ4?t=9858
// https://youtu.be/ERZuLAxZffQ?t=4807 : optimize
// https://youtu.be/8uowVvQ_-Mo?t=1329 : division
const int mod = 1000000007;
struct mint {
  ll x; // typedef long long ll;
  mint(ll x=0):x((x%mod+mod)%mod){}
  mint operator-() const { return mint(-x);}
  mint& operator+=(const mint a) {
    if ((x += a.x) >= mod) x -= mod;
    return *this;
  }
  mint& operator-=(const mint a) {
    if ((x += mod-a.x) >= mod) x -= mod;
    return *this;
  }
  mint& operator*=(const mint a) {
    (x *= a.x) %= mod;
    return *this;
  }
  mint operator+(const mint a) const {
    mint res(*this);
    return res+=a;
  }
  mint operator-(const mint a) const {
    mint res(*this);
    return res-=a;
  }
  mint operator*(const mint a) const {
    mint res(*this);
    return res*=a;
  }
  mint pow(ll t) const {
    if (!t) return 1;
    mint a = pow(t>>1);
    a *= a;
    if (t&1) a *= *this;
    return a;
  }

  // for prime mod
  mint inv() const {
    return pow(mod-2);
  }
  mint& operator/=(const mint a) {
    return (*this) *= a.inv();
  }
  mint operator/(const mint a) const {
    mint res(*this);
    return res/=a;
  }
};

const int MAX = 1000005;

int gcd( int a, int b) {
  if (a % b == 0) {
    return b;
  }
  else {
    return (gcd(b, a%b));
  }
}

int lcm (int a, int b) {
  return a * b / gcd(a, b);
}

//エラトステネスのふるい
struct Sieve {
  int n;
  vector<int> f, primes;
  Sieve(int n = 1): n(n), f(n + 1) {
    f[0] = f[1] = -1;
    for (int i = 2; i <= n; i++) {
      if (f[i]) continue; //印がなければ素数扱い
      primes.push_back(i);
      for (int j = i; j <= n; j += i) {
        f[j] = i; //iの倍数のところに印をつけていく
      }
    }
  }

  bool isPrime(int x) { return f[x] == x; }

  //ｘを素因数分解する関数
  // return -> 素因数
  vector<int> factorList(int x) {
    vector<int> res;
    while (x != 1) {
      res.push_back(f[x]);
      x /= f[x];
    }
    return res; //大きい順で素因数がvectorに格納されて出てくる
  }

  //各素因数が何乗されているかをpair typeで返す
  vector<P> factorPower(int x) {
    vector<int> factors = factorList(x);
    if (factors.size() == 0) return {};
    vector<P> res(1, P(factors[0], 0));
    for (int p : factors) {
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
    Sieve sieve(1e6);
    int n;
    cin >> n;
    vector<int> a(n);

    for (int i = 0; i < n; i++) cin >> a[i];

    map<int, int> mp;
    for (int i = 0; i < n; i++){
      auto f = sieve.factorPower(a[i]);
      for (auto p : f) {
        mp[p.first] = max(mp[p.first], p.second);
        //各数の素因数の累乗のうち、最大乗されているものをすべてかければ最大公倍数になる
        //よって各素数の最大累乗だけmapに格納する
      }
    }

    mint lcm = 1;
    for (auto p: mp) {
      rep(i, p.second) { lcm *= p.first; } //最大公約数がでる
    }

    mint ans;
    rep(i, n) {
      mint b = lcm / a[i];
      ans += b;
    }

    cout << ans.x << endl;
    return 0;
  }
