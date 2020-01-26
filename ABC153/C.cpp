#include <bits/stdc++.h>
#define rep(i, n) for(long long i = 0; i < n; i++)
using namespace std;
using ll = long long;

void vprint(vector<ll> v) {
  for (int i = 0; i < v.size(); i++) {
    cout << v[i];
  }
  cout << endl;
}

int main() {
  ll N, K;
  ll sum = 0;
  cin >> N >> K;
  vector<ll> H(N);
  rep(i, N) cin >> H[i];

  sort(H.begin(), H.end());//小さい順

  rep(i, K) H.pop_back();

  if (H.size() == 0) {
    cout << 0 << endl;
  }
  else {
    rep(i, N - K) sum += H[i];
    
    cout << sum << endl;
  }
  return 0;

}
