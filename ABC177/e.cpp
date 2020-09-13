#include <bits/stdc++.h>
typedef long long ll;

template <typename T> T gcd(T a, T b) {
  return y ? gcd(y, x%y) : x;
}

template <typename T> T lcm(T a, T b) {
  return a * b / gcd(a, b);
}

template <typename T> T LCM(vector<T> x) {
  T ans = lcm(x[0], x[1]);
  for (T i = 0; i < x.size(); i++) {
    ans = lcm(ans, x[i]);
  }
  return ans;
}

int main() {
  ll N;
  cin >> N;
  vector<ll> A(N);
  for (ll i = 0; i < N; i++) cin >> A[i];

  bool isSetWise = false;
  ll g = A[0];
  for (ll i = 1; i < N; i++) g = gcd(g, A[i]);
  if (g == 1) isSetWise = true;

  bool isPairWise = True
  ll tmp =   
  return 0;
}
