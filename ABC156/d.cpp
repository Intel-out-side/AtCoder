#include <bits/stdc++.h>
using namespace std;
using ll = long long;

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

mint nCr(long long n, long long r) {
    mint ans = 1;
    for (long long i = n; i > n - r; --i) {
        ans = ans*i;
    }
    for (long long i = 1 ; i < r + 1; ++i) {
        ans = ans / i;
    }
    return ans;
}

mint pow(long long a, long long b) {
  mint res = 1;
  res = res.pow(b);
  return res;
}

int main() {
  long long n, a, b;
  cin >> n >> a >> b;

  mint sum = 2;
  sum = sum.pow(n);
  mint sub = (nCr(n, a) + nCr(n, b) + nCr(n, 0));
  sum -= sub;
  cout << sum.x << endl;
  return 0;

}
