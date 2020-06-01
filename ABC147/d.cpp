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

int main() {
  ll N;
  cin >> N;
  ll A[N+1];

  for (ll i = 1; i <= N; i++) cin >> A[i];

  mint ruiseki[N+1];
  ruiseki[N] = A[N];
  //ll seki[N+1];
  //seki[N] = A[N];
  for (ll i = N-1; i >= 1; i--) ruiseki[i] += ruiseki[i+1];
  //for (ll i = N-1; i >= 1; i--) seki[i] = ((seki[i]&seki[i+1])<<1);

  mint ans = mint(0);
  for (ll i = 1; i <= N-1; i++) {
    ans += (N-i)*A[i];
    ans += ruiseki[i+1];
  }

  cout << ans.x << endl;
  return 0;
}
