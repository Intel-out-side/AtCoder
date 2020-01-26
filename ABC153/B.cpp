#include <bits/stdc++.h>
#define rep(i, n) for(int i = 0; i < n; i++)
using namespace std;
using ll = long long;

int main() {
  ll H, N;
  cin >> H >> N;
  vector<int> A(N);
  for (ll i = 0; i < N; i++) cin >> A[i];

  for (ll i = 0; i < N; i++) {
    H -= A[i];
  }

  if (H <= 0) cout << "Yes" << endl;
  else cout << "No" << endl;

  return 0;
}
