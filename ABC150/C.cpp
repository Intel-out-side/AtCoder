#include <bits/stdc++.h>
#define rep(i, n) for(int i = 0; i < n; i++)
using namespace std;
using ll = long long;

vector<vector<ll>> permutation(vector<ll> v) {
  vector<vector<ll>> perms;
  do {
    perms.push_back(v);
  } while (next_permutation(v.begin(), v.end()));

  return perms;
}

template <typename T> T VecToInt(vector<T> v) {
  T result = 0, base = 1;
  while (v.size() != 0) {
    result += v[v.size()-1] * base;
    base *= 10;
    v.pop_back();
  }

  return result;
}

int main() {
  int N;
  cin >> N;
  vector<ll> perms(N);
  rep(i, N) perms[i] = i+1;
  vector<vector<ll>> all_perms = permutation(perms);

  vector<ll> P(N), Q(N);
  rep(i, N) cin >> P[i];
  ll p = VecToInt(P);
  rep(i, N) cin >> Q[i];
  ll q = VecToInt(Q);

  ll a, b;
  for (int i = 0; i < all_perms.size(); i++) {
    ll inPerm = VecToInt(all_perms[i]);
    if (inPerm == p) a = i;
    if (inPerm == q) b = i;
  }

  cout << abs(a - b) << endl;
  return 0;
}
