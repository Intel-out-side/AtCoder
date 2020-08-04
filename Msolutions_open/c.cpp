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
  int N, K;
  cin >> N >> K;

  vector<mint> A(N, mint(0));
  for (int i = 0; i < N; i++) {
    ll tmp;
    cin >> tmp;
    A[i] = mint(tmp);
  }

  vector<mint> score(N, mint(0));
  deque<mint> dq;

  mint score_now = mint(1);

  for (int i = 0; i < K; i++) {
    dq.push_back(mint(A[i]));
    score_now *= A[i];
  }

  for (int j = K-1; j < N-1; j++) {
    score[j] = score_now;
    mint left = dq.front();
    dq.pop_front();
    score_now = score_now / left;
    dq.push_back(mint(A[j+1]));
    score_now *= A[j+1];
  }

  score[N-1] = score_now;

  for (int k=K; k < N; k++) {
    if (score[k].x > score[k-1].x) cout << "Yes" << endl;
    else cout << "No" << endl;
  }

  return 0;
}
