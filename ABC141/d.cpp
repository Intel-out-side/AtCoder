#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
  ll N, M;
  cin >> N >> M;
  vector<double> A(N);
  for (ll i = 0; i < N; i++) cin >> A[i];

  for (ll i = 0; i < M; i++) {
    sort(A.begin(), A.end());
    A[N-1] /= 2;
  }

  ll sum = 0;
  for (ll i = 0; i < N; i++) {
    sum += (ll)A[i];
  }

  cout << sum << endl;
  return 0;
}
